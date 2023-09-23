import os
import sys
from collections import Counter
from functools import reduce
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.constants import ALPHABET
from utils.setup import read_inputs

FULL_ALPHA = ALPHABET + ALPHABET.upper()

def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def part_1(override_inputs = None):
    rucksacks = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = 0

    for rucksack in rucksacks:
        split_index = len(rucksack) // 2
        common = Counter(rucksack[:split_index]) & Counter(rucksack[split_index:])
        output += sum(FULL_ALPHA.index(element) + 1 for element, _ in common.items())

    return output


def part_2(override_inputs = None):
    rucksacks = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = 0

    grouped_rucksacks = zip(*([iter(Counter(rucksack) for rucksack in rucksacks)] * 3))
    for group in grouped_rucksacks:
        common = reduce(lambda a, b: a & b, [Counter(rucksack) for rucksack in group])
        output += sum(FULL_ALPHA.index(element) + 1 for element, _ in common.items())

    return output


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
