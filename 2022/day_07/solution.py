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
    index = 0

    while index < len(lines):
        line = lines[index]
        cmd = line.split()[1]

        if cmd == 'cd':
            dir = line.split()[-1]
            directory_stack.pop() if dir == '..' else directory_stack.append(dir)
            index += 1

        elif cmd == 'ls':
            index += 1

            # Break in case this is the last command and the directory is empty.
            if index >= len(lines):
                break

            while index < len(lines) and lines[index][0] != '$':
                if re.match(r'\d', lines[index]):
                    for i in range(0, len(directory_stack)):
                        directory_sizes['/'.join(directory_stack[:i + 1])] += int(lines[index].split()[0])
                index += 1

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
