import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from collections import defaultdict
from utils.setup import read_inputs


def parse_input(input: str):
    register, direction, amount, _, condition_a, comparator, condition_b = input.strip().split(' ')
    return {
        'register': register,
        'amount': int(amount) * (1 if direction == 'inc' else -1),
        'condition': {
            'arguments': [condition_a, int(condition_b)],
            'comparator': comparator
        }
    }


def get_inputs():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parse_input(line) for line in read_inputs(script_directory)]


def check_condition(registers, condition):
    comparator = condition['comparator']
    if comparator == '>':
        return registers[condition['arguments'][0]] > condition['arguments'][1]
    elif comparator == '<':
        return registers[condition['arguments'][0]] < condition['arguments'][1]
    elif comparator == '>=':
        return registers[condition['arguments'][0]] >= condition['arguments'][1]
    elif comparator == '<=':
        return registers[condition['arguments'][0]] <= condition['arguments'][1]
    elif comparator == '==':
        return registers[condition['arguments'][0]] == condition['arguments'][1]
    elif comparator == '!=':
        return registers[condition['arguments'][0]] != condition['arguments'][1]


def part_1(override_inputs = None):
    commands = override_inputs or get_inputs()

    registers = defaultdict(int)

    for command in commands:
        if check_condition(registers, command['condition']):
            registers[command['register']] += command['amount']

    return max(registers.values())


def part_2(override_inputs = None):
    commands = override_inputs or get_inputs()

    registers = defaultdict(int)
    highest_value = 0

    for command in commands:
        if check_condition(registers, command['condition']):
            registers[command['register']] += command['amount']
            highest_value = max(highest_value, registers[command['register']])

    return highest_value


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
