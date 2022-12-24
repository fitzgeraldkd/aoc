import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]


def get_power_level(serial, x, y):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level = (power_level // 100) % 10
    power_level -= 5
    return power_level


def part_1(override_inputs = None):
    serial = get_inputs(parse_input) if override_inputs is None else override_inputs

    print(serial)
    power_levels = {}

    for x in range(1, 301):
        for y in range(1, 301):
            power_levels[(x, y)] = get_power_level(serial, x, y)

    max_power = 0
    max_coordinate = None
    for x in range(1, 299):
        for y in range(1, 299):
            # max_power = max(max_power, sum([power_levels[(x + dx, y + dy)] for dx, dy in
            #                                [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]]))
            cluster_power = sum([power_levels[(x + dx, y + dy)] for dx in range(3) for dy in range(3)])
            # cluster_power = sum([power_levels[(x + dx, y + dy)] for dx, dy in
            #                     [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]])
            # if x == 21 and y == 61:
            #     print(cluster_power)
            if cluster_power > max_power:
                max_power = cluster_power
                max_coordinate = f'{x},{y}'

    # print(max_power)
    print(power_levels[(33, 45)])
    return max_coordinate


def part_2(override_inputs = None):
    serial = get_inputs(parse_input) if override_inputs is None else override_inputs

    print(serial)
    power_levels = {}
    board_size = 300

    for x in range(1, board_size + 1):
        for y in range(1, board_size + 1):
            power_levels[(x, y)] = get_power_level(serial, x, y)

    max_power = 0
    max_coordinate = None
    for cell_size in range(1, board_size + 1):
        print(cell_size)
        for x in range(1, board_size - cell_size + 2):
            for y in range(1, board_size - cell_size + 2):
                # max_power = max(max_power, sum([power_levels[(x + dx, y + dy)] for dx, dy in
                #                                [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]]))
                cluster_power = sum([power_levels[(x + dx, y + dy)] for dx in range(cell_size) for dy in range(cell_size)])
                # cluster_power = sum([power_levels[(x + dx, y + dy)] for dx, dy in
                #                     [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]])
                # if x == 21 and y == 61:
                #     print(cluster_power)
                if cluster_power > max_power:
                    max_power = cluster_power
                    max_coordinate = f'{x},{y},{cell_size}'
                    print(max_coordinate)

    # print(max_power)
    # print(power_levels[(33, 45)])
    return max_coordinate


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
