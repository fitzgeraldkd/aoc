import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parse_input(line) for line in read_inputs(script_directory)][0]


def part_1(override_inputs: str = None):
    stream = override_inputs or get_inputs()

    depth = 0
    in_garbage = False
    skip_next = False
    score = 0

    for char in stream:
        if in_garbage:
            if skip_next:
                skip_next = False
                continue
            elif char == '!':
                skip_next = True
            elif char == '>':
                in_garbage = False
        else:
            if char == '<':
                in_garbage = True
            elif char == '{':
                depth += 1
                score += depth
            elif char == '}':
                depth -= 1

    return score


def part_2(override_inputs: str = None):
    stream = override_inputs or get_inputs()

    garbage_length = 0

    in_garbage = False
    skip_next = False

    for char in stream:
        if in_garbage:
            if skip_next:
                skip_next = False
                continue
            elif char == '!':
                skip_next = True
            elif char == '>':
                in_garbage = False
            else:
                garbage_length += 1
        else:
            if char == '<':
                in_garbage = True

    return garbage_length


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
