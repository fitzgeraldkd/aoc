import os
import sys
from collections import Counter
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]


def react(polymer: str):
    remaining_units = []

    for char in polymer:
        if char.swapcase() == (remaining_units[-1] if remaining_units else None):
            remaining_units.pop()
        else:
            remaining_units.append(char)

    return remaining_units


def part_1(override_inputs = None):
    polymer: str = get_inputs(parse_input) if override_inputs is None else override_inputs
    return len(react(polymer))


def part_2(override_inputs = None):
    polymer: str = get_inputs(parse_input) if override_inputs is None else override_inputs
    polymer = ''.join(react(polymer))

    units = set(polymer.lower())

    shortest_length = len(polymer)
    for unit in units:
        trimmed_polymer = polymer.replace(unit, '').replace(unit.upper(), '')
        shortest_length = min(shortest_length, len(react(trimmed_polymer)))

    return shortest_length


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
