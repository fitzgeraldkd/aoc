import os
from typing import List


def parse_input(input):
    return [int(dimension) for dimension in input.strip().split('x')]


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1(override_inputs: List[List[int]] = None):
    inputs = override_inputs or get_inputs()

    total_area = 0
    for input in inputs:
        [l, w, h] = input
        area = (2*l*w + 2*w*h + 2*h*l)
        slack = int(l * w * h / max(input))
        total_area += area + slack

    return total_area


def part_2(override_inputs: List[List[int]] = None):
    inputs = override_inputs or get_inputs()

    total_length = 0
    for input in inputs:
        [l, w, h] = input
        ribbon = 2 * (l + w + h - max(input))
        bow = l * w * h
        total_length += ribbon + bow

    return total_length


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
