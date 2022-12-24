from typing import Callable

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs(parser: Callable) -> int:
    return [parser(line) for line in read_inputs(__file__)][0]


def part_1(override_inputs: int = None):
    number_of_steps = get_inputs(parse_input) if override_inputs is None else override_inputs

    number_of_repetitions = 2017
    spinlock = [0]
    index = 0

    for i in range(number_of_repetitions):
        index = (index + number_of_steps) % len(spinlock) + 1
        spinlock.insert(index, i + 1)

    return spinlock[(index + 1) % len(spinlock)]


def part_2(override_inputs: int = None):
    number_of_steps = get_inputs(parse_input) if override_inputs is None else override_inputs

    number_of_repetitions = 5000000
    index = 0
    value_at_index_1 = None

    for i in range(number_of_repetitions):
        index = (index + number_of_steps) % (i + 1) + 1
        if index == 1:
            value_at_index_1 = i + 1

    return value_at_index_1


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
