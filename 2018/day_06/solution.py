import math
import os
import sys
from collections import Counter
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs

PART_2_TARGET_DISTANCE = 10000


def parse_input(input: str):
    return tuple(int(coordinate) for coordinate in input.strip().split(', '))


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def get_bounding_box(coordinates):
    min_x = min(coordinates, key=lambda coordinate: coordinate[0])[0]
    max_x = max(coordinates, key=lambda coordinate: coordinate[0])[0]
    min_y = min(coordinates, key=lambda coordinate: coordinate[1])[1]
    max_y = max(coordinates, key=lambda coordinate: coordinate[1])[1]
    return min_x, max_x, min_y, max_y


def part_1(override_inputs = None):
    coordinates = get_inputs(parse_input) if override_inputs is None else override_inputs

    min_x, max_x, min_y, max_y = get_bounding_box(coordinates)

    board = {}
    infinite_regions = set()

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            closest_distance = math.inf
            closest_coordinate = None
            for coordinate in coordinates:
                distance = abs(coordinate[0] - x) + abs(coordinate[1] - y)
                if distance < closest_distance:
                    closest_distance = distance
                    closest_coordinate = coordinate
                elif distance == closest_distance:
                    closest_coordinate = None
            board[(x, y)] = closest_coordinate
            if closest_coordinate is not None and (x in [min_x, max_x] or y in [min_y, max_y]):
                infinite_regions.add(closest_coordinate)

    counted_board = Counter(board.values())
    for coordinate in infinite_regions:
        del counted_board[coordinate]

    return counted_board.most_common(1)[0][1]


def part_2(override_inputs = None):
    """
    Note: this solution will not work if the region extends past the bounding box around the coordinates.
    """
    coordinates = get_inputs(parse_input) if override_inputs is None else override_inputs

    min_x, max_x, min_y, max_y = get_bounding_box(coordinates)

    region_size = 0

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            total_distance = sum(abs(coordinate[0] - x) + abs(coordinate[1] - y) for coordinate in coordinates)
            region_size += 1 if total_distance < PART_2_TARGET_DISTANCE else 0

    return region_size


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
