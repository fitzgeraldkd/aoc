import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.lists import split
from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    initial_state, notes = split(read_inputs(__file__), '\n')
    notes = [note.split(' => ') for note in notes]
    plants = { item for index, item in enumerate(initial_state.split(': ')[1]) if item == '#' }
    notes = { pattern: output for pattern, output in notes }
    return [parser(line) for line in read_inputs(__file__)]


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    return None


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
