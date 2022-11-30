import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.constants import ALPHABET
from utils.setup import read_inputs


def parse_argument(argument: str):
    return argument if argument in ALPHABET else int(argument)


def parse_input(input: str):
    command, arguments = input.strip().split(' ', 1)
    return command, [parse_argument(argument) for argument in arguments.split(' ')]



def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


class Registers:
    def __init__(self):
        self.registers = defaultdict(int)
        self.last_played = None
        self.received_sounds = []

    def get_argument_value(self, argument):
        return argument if isinstance(argument, int) else self.registers[argument]

    def run_instruction(self, command: str, arguments: list):
        if command == 'set':
            self.registers[arguments[0]] = self.get_argument_value(arguments[1])
        elif command == 'sub':
            self.registers[arguments[0]] -= self.get_argument_value(arguments[1])
        elif command == 'mul':
            self.registers[arguments[0]] *= self.get_argument_value(arguments[1])
        elif command == 'jnz':
            if self.get_argument_value(arguments[0]) != 0:
                return self.get_argument_value(arguments[1])
        return 1


def part_1(override_inputs = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    registers = Registers()

    times_multiplied = 0
    index = 0
    while index >= 0 and index < len(instructions):
        if instructions[index][0] == 'mul':
            times_multiplied += 1
        index += registers.run_instruction(*instructions[index])

    print(registers.registers)
    return times_multiplied


def part_2(override_inputs = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    registers = Registers()
    registers.registers['a'] = 1

    index = 0
    
    def chunk_11():
        # Break from chunk when:
        # e = b
        
        # Set f to 0 if:
        # d * e - b = 0
        # e = b / d
        initial_e = registers.registers['e']
        target_e = registers.registers['b'] / registers.registers['d']
        final_e = registers.registers['b']

        if initial_e < target_e and target_e < final_e and target_e == int(target_e):
            registers.registers['f'] = 0
        
        registers.registers['e'] = final_e
        registers.registers['g'] = 0

    def chunk_10():
        # Break from chunk when:
        # d - b = 0
        pass

    while index >= 0 and index < len(instructions):
    
        if index == 11:
            chunk_11()
            index += 9

        index += registers.run_instruction(*instructions[index])

    return registers.registers['h']


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
