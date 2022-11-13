import os
import sys
from typing import Callable, List

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs

LENGTH = 256


def parse_input(input: str):
    return [int(length) for length in input.strip().split(',')]


def parse_input_ascii(input: str):
    return [ord(char) for char in input.strip()]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]


def get_starting_list():
    return [i for i in range(LENGTH)]


def process_rounds(knot_list: List[int], lengths: List[int], number_of_rounds: int = 1):
    position = 0
    skip_size = 0

    for _ in range(number_of_rounds):
        for length in lengths:
            sub_list = []

            for i in range(length):
                index = (position + i) % LENGTH
                sub_list.append(knot_list[index])
            sub_list.reverse()

            for i in range(length):
                index = (position + i) % LENGTH
                knot_list[index] = sub_list[i]

            position = (position + length + skip_size) % LENGTH
            skip_size += 1


def part_1(override_inputs: List[int] = None):
    lengths = get_inputs(parse_input) if override_inputs is None else override_inputs

    knot_list = get_starting_list()
    process_rounds(knot_list, lengths)

    return knot_list[0] * knot_list[1]


def part_2(override_inputs: str = None):
    lengths = get_inputs(parse_input_ascii) if override_inputs is None else parse_input_ascii(override_inputs)
    lengths.extend([17, 31, 73, 47, 23])

    knot_list = get_starting_list()

    process_rounds(knot_list, lengths, number_of_rounds=64)

    dense_hash = []
    for group in range(16):
        new_value = 0
        for sub_index in range(16):
            index = group * 16 + sub_index
            new_value = new_value ^ knot_list[index]

        hex_value = hex(new_value)[2:]
        dense_hash.append(f'{"0" if len(hex_value) == 1 else ""}{hex_value}')

    return ''.join(dense_hash)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
