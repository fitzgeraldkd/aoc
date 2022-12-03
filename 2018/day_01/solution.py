import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    changes = get_inputs(parse_input) if override_inputs is None else override_inputs
    return sum(changes)


def part_2(override_inputs = None):
    changes = get_inputs(parse_input) if override_inputs is None else override_inputs

    frequency = 0
    previous = { 0 }
    index = 0

    while True:
        frequency += changes[index]
        if frequency in previous:
            return frequency
        else:
            previous.add(frequency)
        index = (index + 1) % len(changes)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
