import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return [int(value) for value in input.strip().split()]


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)][0]


def part_1(override_inputs = None):
    nodes = get_inputs(parse_input) if override_inputs is None else override_inputs

    index = 0
    metadata_total = 0
    stack = []
    while index < len(nodes):
        if len(stack) == 0 or stack[-1][0] > 0:
            if stack:
                stack[-1][0] -= 1
            stack.append([nodes[index], nodes[index + 1]])
            index += 2
        else:
            metadata_nodes = nodes[index:index + stack[-1][1]]
            metadata_total += sum(metadata_nodes)
            stack.pop()
            index += len(metadata_nodes)

    return metadata_total


def part_2(override_inputs = None):
    nodes = get_inputs(parse_input) if override_inputs is None else override_inputs

    index = 0
    stack = []
    children = []
    while index < len(nodes):
        if len(stack) == 0 or stack[-1][0] > 0:
            if stack:
                stack[-1][0] -= 1
            stack.append([nodes[index], nodes[index + 1]])
            children.append([])
            index += 2
        else:
            metadata_nodes = nodes[index:index + stack[-1][1]]
            if children[-1]:
                new_child = sum(children[-1][metadata_index - 1] for metadata_index in metadata_nodes if metadata_index <= len(children[-1]))
            else:
                new_child = sum(metadata_nodes)

            children.pop()
            stack.pop()
            index += len(metadata_nodes)

            if children:
                children[-1].append(new_child)
            else:
                return new_child


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
