import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)][0]


def is_marker(characters: str):
    return len(characters) == len(set(characters))


def part_1(override_inputs = None):
    datastream = get_inputs(parse_input) if override_inputs is None else override_inputs

    marker_length = 4
    for index in range(marker_length, len(datastream)):
        if is_marker(datastream[index - marker_length:index]):
            return index


def part_2(override_inputs = None):
    datastream = get_inputs(parse_input) if override_inputs is None else override_inputs

    marker_length = 14
    for index in range(marker_length, len(datastream)):
        if is_marker(datastream[index - marker_length:index]):
            return index


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
