import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    _, quantity, _, source, _, destination = input.strip().split()
    return [int(value) for value in [quantity, source, destination]]


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    # TODO: Parse initial stacks from the inputs instead of hard-coding.
    stacks = [
        ['N', 'R', 'G', 'P'],
        ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
        ['M', 'S', 'V'],
        ['L', 'S', 'R', 'C', 'Z', 'P'],
        ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
        ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
        ['H', 'D', 'G', 'W', 'P'],
        ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
        ['R', 'P', 'F', 'L', 'W', 'G', 'Z']
    ]

    for quantity, source, destination in inputs:
        for _ in range(quantity):
            stacks[destination - 1].append(stacks[source - 1].pop())

    return ''.join(stack.pop() for stack in stacks)


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    # TODO: Parse initial stacks from the inputs instead of hard-coding.
    stacks = [
        ['N', 'R', 'G', 'P'],
        ['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],
        ['M', 'S', 'V'],
        ['L', 'S', 'R', 'C', 'Z', 'P'],
        ['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],
        ['C', 'T', 'N', 'W', 'D', 'M', 'S'],
        ['H', 'D', 'G', 'W', 'P'],
        ['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],
        ['R', 'P', 'F', 'L', 'W', 'G', 'Z']
    ]

    for quantity, source, destination in inputs:
        stacks[destination - 1].extend(stacks[source - 1][-1 * quantity:])
        stacks[source - 1] = stacks[source - 1][:-1 * quantity]

    return ''.join(stack.pop() for stack in stacks)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
