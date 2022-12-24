import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return [[int(position) for position in elf.split('-')] for elf in input.strip().split(',')]


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def part_1(override_inputs = None):
    pairs = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = 0

    for pair in pairs:
        if (pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]) or \
                (pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]):
            output += 1

    return output


def part_2(override_inputs = None):
    pairs = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = 0

    for pair in pairs:
        if not (pair[0][1] < pair[1][0] or pair[0][0] > pair[1][1]):
            output += 1

    return output


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
