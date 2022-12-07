import os
import re
import sys
from collections import defaultdict
from typing import Callable, List

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def get_directory_sizes(lines: List[str]):
    directory_stack = []
    directory_sizes = defaultdict(int)

    for line in lines:

        if line[0] == '$' and line.split()[1] == 'cd':
            dir = line.split()[-1]
            directory_stack.pop() if dir == '..' else directory_stack.append(dir)

        elif re.match(r'\d', line):
            for i in range(0, len(directory_stack)):
                directory_sizes['/'.join(directory_stack[:i + 1])] += int(line.split()[0])

    return directory_sizes


def part_1(override_inputs = None):
    lines = get_inputs(parse_input) if override_inputs is None else override_inputs

    directory_sizes = get_directory_sizes(lines)

    return sum([size for size in directory_sizes.values() if size <= 100000])


def part_2(override_inputs = None):
    lines = get_inputs(parse_input) if override_inputs is None else override_inputs

    directory_sizes = get_directory_sizes(lines)

    used_space = directory_sizes['/']
    total_space = 70000000
    required_space = 30000000
    amount_to_delete = required_space - (total_space - used_space)

    return min([size for size in directory_sizes.values() if size >= amount_to_delete])


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
