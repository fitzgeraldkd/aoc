import math
import operator
import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import get_direction, get_manhattan_distance
from utils.setup import read_inputs

SAND_ORIGIN = (500, 0)

def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    rocks = defaultdict(lambda: None)
    script_directory = os.path.dirname(os.path.realpath(__file__))
    for line in read_inputs(script_directory):
        str_coords = line.split(' -> ')
        coords = [tuple(int(coord) for coord in pair.split(',')) for pair in str_coords]
        for i in range(len(coords) - 1):
            direction = get_direction(coords[i], coords[i + 1])
            distance = get_manhattan_distance(coords[i], coords[i + 1])
            current = coords[i]
            for j in range(distance + 1):
                rocks[current] = '#'
                if j != distance:
                    current = tuple(map(operator.add, current, direction))

    return rocks


def get_floor(board, start):
    floor_height = math.inf
    for coord in board:
        if coord[0] == start[0] and coord[1] > start[1] and coord[1] < floor_height:
            floor_height = coord[1]
    return (start[0], floor_height - 1)


def drop_sand(board):
    sand = get_floor(board, SAND_ORIGIN)

    while sand[1] != math.inf and board[SAND_ORIGIN] is None:
        down_left = (sand[0] - 1, sand[1] + 1)
        down_right = (sand[0] + 1, sand[1] + 1)
        if board[down_left] is None:
            sand = get_floor(board, down_left)
        elif board[down_right] is None:
            sand = get_floor(board, down_right)
        else:
            break

    if sand[1] == math.inf or board[SAND_ORIGIN] is not None:
        return 'FULL'

    board[sand] = 'O'


def part_1(override_inputs = None):
    board = get_inputs(parse_input) if override_inputs is None else override_inputs

    grains_added = 0
    while True:
        if drop_sand(board) == 'FULL':
            return grains_added
        grains_added += 1


def part_2(override_inputs = None):
    board = get_inputs(parse_input) if override_inputs is None else override_inputs

    lowest_floor = max(board.keys(), key=lambda coord: coord[1])[1]

    grains_added = 1
    board[SAND_ORIGIN] = 'O'
    row = 1

    for row in range(1, lowest_floor + 2):
        for x in range(SAND_ORIGIN[0] - row, SAND_ORIGIN[0] + row + 1):
            if board[(x, row)] is not None:
                continue
            points_above = [(x, row - 1), (x - 1, row - 1), (x + 1, row - 1)]
            if any(board[point] == 'O' for point in points_above):
                board[(x, row)] = 'O'
                grains_added += 1

    return grains_added


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
