import math
import operator
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


DIRECTION_ORDER = ['N', 'S', 'W', 'E']
DIRECTION_MAP = {
    'N': (0, -1),
    'S': (0, 1),
    'W': (-1, 0),
    'E': (1, 0)
}
DIRECTION_CHECKS = {
    'N': [(-1, -1), (0, -1), (1, -1)],
    'S': [(-1, 1), (0, 1), (1, 1)],
    'W': [(-1, -1), (-1, 0), (-1, 1)],
    'E': [(1, -1), (1, 0), (1, 1)],
}
DIRECTIONS = [
    (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0)
]


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    grid = get_inputs(parse_input) if override_inputs is None else override_inputs
    elves = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                elves.add((x, y))

    direction_order = [*DIRECTION_ORDER]
    for _ in range(10):
        elves_to_move = [elf for elf in elves if any((tuple(map(operator.add, elf, direction)) in elves) for direction in DIRECTIONS)]
        elf_movements = {}
        destinations = set()
        for elf in elves_to_move:
            for direction in direction_order:
                if all((tuple(map(operator.add, elf, neighbor)) not in elves) for neighbor in DIRECTION_CHECKS[direction]):
                    destination = tuple(map(operator.add, elf, DIRECTION_MAP[direction]))
                    if destination in destinations:
                        for key in list(elf_movements.keys()):
                            if elf_movements[key] == destination:
                                del elf_movements[key]
                    else:
                        elf_movements[elf] = destination
                        destinations.add(destination)
                    break

        for elf, destination in elf_movements.items():
            elves.remove(elf)
            elves.add(destination)

        direction_order = [*direction_order[1:], direction_order[0]]

    min_x, max_x, min_y, max_y = math.inf, -math.inf, math.inf, -math.inf
    for elf in elves:
        min_x = min(min_x, elf[0])
        max_x = max(max_x, elf[0])
        min_y = min(min_y, elf[1])
        max_y = max(max_y, elf[1])

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


def part_2(override_inputs = None):
    grid = get_inputs(parse_input) if override_inputs is None else override_inputs
    elves = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                elves.add((x, y))

    direction_order = [*DIRECTION_ORDER]
    for i in range(1000000):
        elves_to_move = [elf for elf in elves if any((tuple(map(operator.add, elf, direction)) in elves) for direction in DIRECTIONS)]
        elf_movements = {}
        destinations = set()
        for elf in elves_to_move:
            for direction in direction_order:
                if all((tuple(map(operator.add, elf, neighbor)) not in elves) for neighbor in DIRECTION_CHECKS[direction]):
                    destination = tuple(map(operator.add, elf, DIRECTION_MAP[direction]))
                    if destination in destinations:
                        for key in list(elf_movements.keys()):
                            if elf_movements[key] == destination:
                                del elf_movements[key]
                    else:
                        elf_movements[elf] = destination
                        destinations.add(destination)
                    break

        if len(elf_movements.keys()) == 0:
            return i + 1

        for elf, destination in elf_movements.items():
            elves.remove(elf)
            elves.add(destination)

        direction_order = [*direction_order[1:], direction_order[0]]

    min_x, max_x, min_y, max_y = math.inf, -math.inf, math.inf, -math.inf
    for elf in elves:
        min_x = min(min_x, elf[0])
        max_x = max(max_x, elf[0])
        min_y = min(min_y, elf[1])
        max_y = max(max_y, elf[1])

    return (max_x - min_x + 1) * (max_y - min_y + 1) - len(elves)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
