import math
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import a_star
from utils.setup import read_inputs
from utils.constants import ALPHABET


def parse_input(input: str):
    return list(input.strip())


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def get_heuristic(location: tuple, goal: tuple):
    return abs(location[0] - goal[0]) + abs(location[1] - goal[1])


def get_is_wall(neighbor, current, grid):
    if neighbor[0] < 0 or neighbor[1] < 0 or neighbor[0] >= len(grid[0]) or neighbor[1] >= len(grid):
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

    return len(a_star(start, end, is_wall, get_heuristic)) - 1


def part_2(override_inputs = None):
    """
    Possible optimization: Sort the possible_starts list by distance from goal (largest first). For any other potential
    start point along the way, their optimal path will have already been determined.

    Also, if a point has no possible path to the goal, all adjacent points of the same elevation will not be possible.
    """
    grid = get_inputs(parse_input) if override_inputs is None else override_inputs

    end = None
    possible_starts = []

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'S':
                possible_starts.append((x, y))
                grid[y][x] = 'a'
            elif cell == 'E':
                end = (x, y)
                grid[y][x] = 'z'
            elif cell == 'a':
                possible_starts.append((x, y))

    is_wall = lambda neighbor, current: get_is_wall(neighbor, current, grid)

    shortest_path = math.inf
    for start in possible_starts:
        path = a_star(start, end, is_wall, get_heuristic)
        if path:
            shortest_path = min(shortest_path, len(path) - 1)

    return shortest_path


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
