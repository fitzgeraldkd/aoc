import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def mix_file(indexed_file):
    for original_index in range(len(indexed_file)):
        item = next(item for item in indexed_file if item[0] == original_index)
        if item[1] % len(indexed_file) == 0:
            continue

        index = indexed_file.index(item)
        new_index = (index + item[1]) % (len(indexed_file) - 1)
        indexed_file.pop(index)
        indexed_file.insert(new_index, item)


def part_1(override_inputs = None):
    encrypted_file = get_inputs(parse_input) if override_inputs is None else override_inputs
    indexed_file = list(enumerate(encrypted_file))

    mix_file(indexed_file)

    mixed_file = [item[1] for item in indexed_file]
    zero_index = mixed_file.index(0)

    return sum(mixed_file[(zero_index + offset) % len(mixed_file)] for offset in [1000, 2000, 3000])


def part_2(override_inputs = None):
    encrypted_file = get_inputs(parse_input) if override_inputs is None else override_inputs
    indexed_file = list(enumerate([value * 811589153 for value in encrypted_file]))

    for _ in range(10):
        mix_file(indexed_file)

    mixed_file = [item[1] for item in indexed_file]
    zero_index = mixed_file.index(0)

    return sum(mixed_file[(zero_index + offset) % len(mixed_file)] for offset in [1000, 2000, 3000])


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
