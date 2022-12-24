from collections import defaultdict
from typing import Callable

from utils.constants import ALPHABET
from utils.setup import read_inputs


def parse_argument(argument: str):
    return argument if argument in ALPHABET else int(argument)


def parse_input(input: str):
    command, arguments = input.strip().split(' ', 1)
    return command, [parse_argument(argument) for argument in arguments.split(' ')]


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def get_argument(argument, registers: dict):
    return argument if isinstance(argument, int) else registers[argument]


class Registers:
    def __init__(self):
        self.registers = defaultdict(int)
        self.last_played = None
        self.received_sounds = []

    def get_argument_value(self, argument):
        return argument if isinstance(argument, int) else self.registers[argument]

    def run_instruction(self, command: str, arguments: list):
        if command == 'snd':
            self.last_played = self.registers[arguments[0]]
        elif command == 'set':
            self.registers[arguments[0]] = self.get_argument_value(arguments[1])
        elif command == 'add':
            self.registers[arguments[0]] += self.get_argument_value(arguments[1])
        elif command == 'mul':
            self.registers[arguments[0]] *= self.get_argument_value(arguments[1])
        elif command == 'mod':
            self.registers[arguments[0]] %= self.get_argument_value(arguments[1])
        elif command == 'rcv':
            if self.registers[arguments[0]] != 0:
                self.received_sounds.append(self.last_played)
        elif command == 'jgz':
            if self.registers[arguments[0]] > 0:
                return self.get_argument_value(arguments[1])


def part_1(override_inputs = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    registers = Registers()

    index = 0
    while index >= 0 and index < len(instructions):
        amount_to_jump = registers.run_instruction(*instructions[index])
        if len(registers.received_sounds) > 0:
            return registers.received_sounds[0]
        index += amount_to_jump if amount_to_jump is not None else 1

    return None


class RegistersPartTwo:
    def __init__(self, id: int, instructions: list, paired_program = None):
        self.registers = defaultdict(int)
        self.registers['p'] = id
        self.last_played = None
        self.times_sent = 0
        self.queue = []
        self.instructions = instructions
        self.instruction_index = 0
        self.paired_program = paired_program

    def get_argument_value(self, argument):
        return argument if isinstance(argument, int) else self.registers[argument]

    def is_running(self):
        return not (self.instruction_index < 0 or
                    self.instruction_index >= len(self.instructions) or
                    (self.instructions[self.instruction_index][0] == 'rcv' and len(self.queue) == 0))

    def run_instruction(self):
        command, arguments = self.instructions[self.instruction_index]
        if command == 'snd':
            self.times_sent += 1
            self.paired_program.queue.append(self.get_argument_value(arguments[0]))
        elif command == 'set':
            self.registers[arguments[0]] = self.get_argument_value(arguments[1])
        elif command == 'add':
            self.registers[arguments[0]] += self.get_argument_value(arguments[1])
        elif command == 'mul':
            self.registers[arguments[0]] *= self.get_argument_value(arguments[1])
        elif command == 'mod':
            self.registers[arguments[0]] %= self.get_argument_value(arguments[1])
        elif command == 'rcv':
            if len(self.queue) == 0:
                return
            else:
                self.registers[arguments[0]] = self.queue.pop(0)
        elif command == 'jgz':
            if self.get_argument_value(arguments[0]) > 0:
                self.instruction_index += self.get_argument_value(arguments[1])
                return

        self.instruction_index += 1


def part_2(override_inputs = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    program_0 = RegistersPartTwo(0, instructions)
    program_1 = RegistersPartTwo(1, instructions, program_0)
    program_0.paired_program = program_1

    while program_0.is_running() or program_1.is_running():
        if program_0.is_running():
            program_0.run_instruction()
        if program_1.is_running():
            program_1.run_instruction()

    print(program_0.registers)
    print(program_1.registers)

    return program_1.times_sent


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
