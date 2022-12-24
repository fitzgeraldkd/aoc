from collections import defaultdict
from typing import Callable

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


STATES = {
    'A': {
        0: {
            'write': 1,
            'move': 1,
            'next': 'B'
        },
        1: {
            'write': 0,
            'move': -1,
            'next': 'E'
        }
    },
    'B': {
        0: {
            'write': 1,
            'move': -1,
            'next': 'C'
        },
        1: {
            'write': 0,
            'move': 1,
            'next': 'A'
        }
    },
    'C': {
        0: {
            'write': 1,
            'move': -1,
            'next': 'D'
        },
        1: {
            'write': 0,
            'move': 1,
            'next': 'C'
        }
    },
    'D': {
        0: {
            'write': 1,
            'move': -1,
            'next': 'E'
        },
        1: {
            'write': 0,
            'move': -1,
            'next': 'F'
        }
    },
    'E': {
        0: {
            'write': 1,
            'move': -1,
            'next': 'A'
        },
        1: {
            'write': 1,
            'move': -1,
            'next': 'C'
        }
    },
    'F': {
        0: {
            'write': 1,
            'move': -1,
            'next': 'E'
        },
        1: {
            'write': 1,
            'move': 1,
            'next': 'A'
        }
    },
}


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    tape = defaultdict(int)
    position = 0
    state = 'A'

    for _ in range(12208951):
        instruction = STATES[state][tape[position]]
        tape[position] = instruction['write']
        position += instruction['move']
        state = instruction['next']

    return sum(tape.values())


def part_2(override_inputs = None):
    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
