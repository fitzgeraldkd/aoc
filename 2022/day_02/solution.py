import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip().split(' ')


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]

WIN = 6
DRAW = 3
LOSE = 0

MOVE_POINTS = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}


def part_1(override_inputs = None):
    rounds = get_inputs(parse_input) if override_inputs is None else override_inputs

    outcome_points = {
        'A': {
            'X': DRAW,
            'Y': WIN,
            'Z': LOSE
        },
        'B': {
            'X': LOSE,
            'Y': DRAW,
            'Z': WIN
        },
        'C': {
            'X': WIN,
            'Y': LOSE,
            'Z': DRAW
        }
    }

    return sum(MOVE_POINTS[me] + outcome_points[elf][me] for elf, me in rounds)


def part_2(override_inputs = None):
    rounds = get_inputs(parse_input) if override_inputs is None else override_inputs

    outcome_points = {
        'X': LOSE,
        'Y': DRAW,
        'Z': WIN
    }

    offset = {
        'X': 2,
        'Y': 0,
        'Z': 1
    }

    return sum((MOVE_POINTS[elf] + offset[outcome] - 1) % 3 + 1 + outcome_points[outcome] for elf, outcome in rounds)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
