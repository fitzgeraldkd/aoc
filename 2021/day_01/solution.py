import os
import sys
from typing import Callable, List

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def count_increases(depths: List[int], sample_size: int):
    return len([None for i in range(0, len(depths) - sample_size) if depths[i + sample_size] > depths[i]])


def part_1(override_inputs = None):
    depths = get_inputs(parse_input) if override_inputs is None else override_inputs
    return count_increases(depths, 1)


def part_2(override_inputs = None):
    depths = get_inputs(parse_input) if override_inputs is None else override_inputs
    return count_increases(depths, 3)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
