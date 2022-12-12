import math
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

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


def get_is_wall(neighbor, current, grid):
    if not is_in_boundaries(neighbor, grid):
        return True
    return ALPHABET.index(grid[neighbor[1]][neighbor[0]]) > ALPHABET.index(grid[current[1]][current[0]]) + 1


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

    is_wall = lambda neighbor, current: get_is_wall(neighbor, current, grid)

    return len(a_star(start, end, is_wall, get_heuristic=get_manhattan_distance)) - 1


def part_2(override_inputs = None):
    grid = get_inputs(parse_input) if override_inputs is None else override_inputs

    end = None
    possible_starts = set()

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                possible_starts.add((x, y))
                grid[y][x] = 'a'
            elif cell == 'E':
                end = (x, y)
                grid[y][x] = 'z'
            elif cell == 'a':
                possible_starts.add((x, y))

    is_wall = lambda neighbor, current: get_is_wall(neighbor, current, grid)

    possible_paths = {}

    def discard_adjacent(coords):
        for adjacent in get_adjacent(coords):
            if is_in_boundaries(adjacent, grid) and adjacent in possible_starts and adjacent not in possible_paths:
                possible_paths[adjacent] = math.inf
                discard_adjacent(adjacent)

    for start in possible_starts:
        if start not in possible_paths:
            path = a_star(start, end, is_wall, get_heuristic=get_manhattan_distance)
            if path is not None:
                possible_paths[start] = len(path)
                for index, node in [(index, node) for index, node in enumerate(path) if node in possible_starts]:
                    possible_paths[node] = index + 1
            else:
                possible_paths[start] = math.inf
                discard_adjacent(start)

    return min(possible_paths.values()) - 1


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
