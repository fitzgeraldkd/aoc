import os
import re
import sys
from typing import Callable, Dict, List, Set

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.lists import split
from utils.setup import read_inputs


PossibleCodeInstructionMap = Dict[int, Set[Callable[[List[int], List[int]], List[int]]]]

class Registers:
    def __init__(self, reg_0 = 0, reg_1 = 0, reg_2 = 0, reg_3 = 0):
        self.values = [reg_0, reg_1, reg_2, reg_3]

    def run_command(self, command: str, *inputs: int):
        getattr(self, command)(*inputs)

    def addr(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] + self.values[inputs[1]]

    def addi(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] + inputs[1]

    def mulr(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] * self.values[inputs[1]]

    def muli(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] * inputs[1]

    def banr(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] & self.values[inputs[1]]

    def bani(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] & inputs[1]

    def borr(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] | self.values[inputs[1]]

    def bori(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]] | inputs[1]

    def setr(self, *inputs: int):
        self.values[inputs[2]] = self.values[inputs[0]]

    def seti(self, *inputs: int):
        self.values[inputs[2]] = inputs[0]

    def gtir(self, *inputs: int):
        self.values[inputs[2]] = 1 if inputs[0] > self.values[inputs[1]] else 0

    def gtri(self, *inputs: int):
        self.values[inputs[2]] = 1 if self.values[inputs[0]] > inputs[1] else 0

    def gtrr(self, *inputs: int):
        self.values[inputs[2]] = 1 if self.values[inputs[0]] > self.values[inputs[1]] else 0

    def eqir(self, *inputs: int):
        self.values[inputs[2]] = 1 if inputs[0] == self.values[inputs[1]] else 0

    def eqri(self, *inputs: int):
        self.values[inputs[2]] = 1 if self.values[inputs[0]] == inputs[1] else 0

    def eqrr(self, *inputs: int):
        self.values[inputs[2]] = 1 if self.values[inputs[0]] == self.values[inputs[1]] else 0


def str_to_int_list(string: str):
    return [int(value) for value in re.split(r',?\s', string.replace('[', '').replace(']', ''))]


def parse_sample(sample: List[str]):
    return [str_to_int_list(line.split('Before: ')[-1].split('After: ')[-1].strip()) for line in sample]


def get_inputs():
    samples, _, test_program = list(split(split(read_inputs(__file__), '\n'), []))
    return [parse_sample(sample) for sample in samples], [str_to_int_list(instruction.strip()) for instruction in test_program[0]]


COMMANDS = ['addr', 'addi', 'banr', 'bani', 'borr', 'bori', 'eqir', 'eqri', 'eqrr', 'gtir', 'gtri', 'gtrr', 'mulr', 'muli', 'setr', 'seti']


def get_possible_operations(before: List[int], instruction: List[int], after: List[int], commands=COMMANDS):
    possible_operations = set()
    for command in commands:
        registers = Registers(*before)
        registers.run_command(command, *instruction[1:])
        if registers.values == after:
            possible_operations.add(command)
    return possible_operations


def part_1(override_inputs = None):
    samples, _ = get_inputs() if override_inputs is None else override_inputs
    return sum(1 if len(get_possible_operations(*sample)) >= 3 else 0 for sample in samples)


def part_2(override_inputs = None):
    samples, instructions = get_inputs() if override_inputs is None else override_inputs
    possible_code_pairs = {i: { *COMMANDS } for i in range(16)}
    for sample in samples:
        possible_operations = get_possible_operations(*sample, possible_code_pairs[sample[1][0]])
        possible_code_pairs[sample[1][0]] &= possible_operations
        if len(possible_operations) == 1:
            command = next(iter(possible_operations))
            for i in range(16):
                if i == sample[1][0]:
                    continue
                possible_code_pairs[i].discard(command)

    registers = Registers()
    for instruction in instructions:
        registers.run_command(next(iter(possible_code_pairs[instruction[0]])), *instruction[1:])
    return registers.values[0]


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
