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


POINTS = {
    'A': 1,
    'B': 2,
    'C': 3,
    'X': 1,
    'Y': 2,
    'Z': 3,
}

DRAW = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

WIN = {
    'Y': 'A',
    'Z': 'B',
    'X': 'C'
}

def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    scores = [0, 0]

    for input in inputs:
        scores[0] += POINTS[input[0]]
        scores[1] += POINTS[input[1]]
        if DRAW[input[0]] == input[1]:
            scores[0] += 3
            scores[1] += 3
        elif WIN[input[1]] == input[0]:
            scores[1] += 6
        else:
            scores[0] += 6

    return scores[1]

LOSE_2 = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

WIN_2 = {
    'A': 'Y',
    'B': 'Z',
    'C': 'X'
}

def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = 0

    for input in inputs:
        elf = input[0]
        if input[1] == 'X':
            me = LOSE_2[elf]
            output += POINTS[me]
        elif input[1] == 'Y':
            me = elf
            output += POINTS[me]
            output += 3
        else:
            me = WIN_2[elf]
            output += POINTS[me] + 6

    return output


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
