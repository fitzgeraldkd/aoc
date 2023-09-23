import os
import re
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.lists import split
from utils.setup import read_inputs


def parse_input(input: str):
    _, quantity, _, source, _, destination = input.strip().split()
    return [int(value) for value in [quantity, source, destination]]


def get_inputs(parser: Callable):
    initial_state, instructions = split(read_inputs(__file__), '\n')
    stacks = []
    for match in re.finditer(r'\d', initial_state[-1]):
        stack = []
        for row in initial_state[-2::-1]:
            if len(row) <= match.start() or row[match.start()] == ' ':
                break
            stack.append(row[match.start()])
        stacks.append(stack)
    return stacks, [parser(line) for line in instructions]


def part_1(override_inputs = None):
    stacks, instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    for quantity, source, destination in instructions:
        for _ in range(quantity):
            stacks[destination - 1].append(stacks[source - 1].pop())

    return ''.join(stack.pop() for stack in stacks)


def part_2(override_inputs = None):
    stacks, instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    for quantity, source, destination in instructions:
        stacks[destination - 1].extend(stacks[source - 1][-1 * quantity:])
        stacks[source - 1] = stacks[source - 1][:-1 * quantity]

    return ''.join(stack.pop() for stack in stacks)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
