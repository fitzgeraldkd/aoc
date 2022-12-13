import math
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue
from utils.pathing import a_star, get_adjacent, get_manhattan_distance
from utils.setup import read_inputs
from utils.constants import ALPHABET


def parse_input(input: str):
    return list(input.strip())


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def is_in_boundaries(coords, grid):
    return min(coords) >= 0 and coords[0] < len(grid[0]) and coords[1] < len(grid)


def part_1(override_inputs = None):
    grid = get_inputs(parse_input) if override_inputs is None else override_inputs

    start = None
    end = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                start = (x, y)
                grid[y][x] = 'a'
            elif cell == 'E':
                end = (x, y)
                grid[y][x] = 'z'

    def is_wall(neighbor, current):
        if not is_in_boundaries(neighbor, grid):
            return True
        return ALPHABET.index(grid[neighbor[1]][neighbor[0]]) > ALPHABET.index(grid[current[1]][current[0]]) + 1

    return len(a_star(start, end, is_wall, get_heuristic=get_manhattan_distance)) - 1


def part_2(override_inputs = None):
    grid = get_inputs(parse_input) if override_inputs is None else override_inputs

    end = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                grid[y][x] = 'a'
            elif cell == 'E':
                end = (x, y)
                grid[y][x] = 'z'

    def is_wall(neighbor, current):
        if not is_in_boundaries(neighbor, grid):
            return True
        return ALPHABET.index(grid[neighbor[1]][neighbor[0]]) + 1 < ALPHABET.index(grid[current[1]][current[0]])

    queue = [(neighbor, 1) for neighbor in get_adjacent(end) if not is_wall(neighbor, end)]
    checked = { end }
    while queue:
        node, distance = queue.pop(0)
        checked.add(node)
        if grid[node[1]][node[0]] == 'a':
            return distance
        else:
            for neighbor in get_adjacent(node):
                if not is_wall(neighbor, node) and neighbor not in checked:
                    queue.append((neighbor, distance + 1))
                    checked.add(neighbor)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
