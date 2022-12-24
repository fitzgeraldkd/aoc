import os
from typing import Callable, Tuple

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip().rsplit(' ', 1)[-1])


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def generator_a(value: int):
    return value * 16807 % 2147483647

def generator_b(value: int):
    return value * 48271 % 2147483647


def next_values(generators: Tuple[int, int]):
    return (
        generator_a(generators[0]),
        generator_b(generators[1])
    )


def next_round(generators: Tuple[int, int]):
    values = []
    for _ in range(5):
        generators = next_values(generators)
        values.append(generators)
    return generators, values


def part_1(override_inputs = None):
    generators = get_inputs(parse_input) if override_inputs is None else override_inputs

    mask = 2 ** 16 - 1
    matches = 0
    for _ in range(40000000):
        generators = next_values(generators)
        if generators[0] & mask == generators[1] & mask:
            matches += 1

    return matches


def part_2(override_inputs = None):
    generator_a_value, generator_b_value = get_inputs(parse_input) if override_inputs is None else override_inputs

    NUMBER_OF_PAIRS = 5000000

    generator_a_values = []
    generator_b_values = []

    while len(generator_a_values) < NUMBER_OF_PAIRS:
        generator_a_value = generator_a(generator_a_value)
        if generator_a_value % 4 == 0:
            generator_a_values.append(generator_a_value)

    while len(generator_b_values) < NUMBER_OF_PAIRS:
        generator_b_value = generator_b(generator_b_value)
        if generator_b_value % 8 == 0:
            generator_b_values.append(generator_b_value)

    mask = 2 ** 16 - 1
    matches = 0
    for i in range(NUMBER_OF_PAIRS):
        if generator_a_values[i] & mask == generator_b_values[i] & mask:
            matches += 1

    return matches


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
