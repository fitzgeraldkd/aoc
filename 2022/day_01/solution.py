import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip()) if input.strip() != '' else None


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    inputs.append(None)

    this_sum = 0
    max_sum = 0
    for input in inputs:
        if input is None:
            max_sum = max(max_sum, this_sum)
            this_sum = 0
        else:
            this_sum += input

    return max_sum


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    inputs.append(None)

    this_sum = 0
    sums = []
    for input in inputs:
        if input is None:
            sums.append(this_sum)
            this_sum = 0
        else:
            this_sum += input

    return sum(sorted(sums, reverse=True)[:3])


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
