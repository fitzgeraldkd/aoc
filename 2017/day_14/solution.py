import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from day_10.solution import part_2 as knot_hash
from utils.numbers import get_padded_binary
from utils.pathing import get_adjacent
from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable) -> str:
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]


def get_grid(key: str):
    grid = []
    for i in range(128):
        hash = knot_hash(f'{key}-{i}')
        grid.append(''.join(get_padded_binary(char, 4, 16) for char in hash))
    return grid


def part_1(override_inputs: str = None):
    key = get_inputs(parse_input) if override_inputs is None else override_inputs

    grid = get_grid(key)

    return sum(row.count('1') for row in grid)


def part_2(override_inputs: str = None):
    key = get_inputs(parse_input) if override_inputs is None else override_inputs

    grid = get_grid(key)
    groups = 0
    coords_to_check = set()

    for y, row in enumerate(grid):
        for x, char in enumerate(row):
            if char == '1':
                coords_to_check.add((x, y))

    while len(coords_to_check) > 0:
        groups += 1
        coord_to_check = coords_to_check.pop()
        checked_neighbors = set()
        neighbors_to_check = set()

        for neighbor in get_adjacent(coord_to_check):
            if neighbor in coords_to_check:
                neighbors_to_check.add(neighbor)

        while len(neighbors_to_check) > 0:
            neighbor = neighbors_to_check.pop()
            checked_neighbors.add(neighbor)
            if neighbor in coords_to_check:
                coords_to_check.remove(neighbor)
                for next_neighbor in get_adjacent(neighbor):
                    if next_neighbor not in checked_neighbors:
                        neighbors_to_check.add(next_neighbor)

    return groups


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())