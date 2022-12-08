import operator
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import DIRECTIONS
from utils.setup import read_inputs


def parse_input(input: str):
    return [int(height) for height in input.strip()]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def get_tall_trees(forest_map):
    visible_map = [[False for _ in range(len(forest_map[0]))] for _ in range(len(forest_map))]

    for y in range(len(forest_map)):
        for x in range(len(forest_map[0])):
            this_height = forest_map[y][x]

            checks = [
                [0, x, y, y + 1],
                [x + 1, None, y, y + 1],
                [x, x + 1, 0, y],
                [x, x + 1, y + 1, None]
            ]

            for x_min, x_max, y_min, y_max in checks:
                trees = [height for group in forest_map[y_min:y_max] for height in group[x_min:x_max]]
                if not trees or max(trees) < this_height:
                    visible_map[y][x] = True
                    break

    # The code below is faster, but less pretty...
    # for y, row in enumerate(forest_map):
    #     prev_height = -1
    #     for x, height in enumerate(row):
    #         if height > prev_height:
    #             visible_map[y][x] = True
    #             prev_height = height

    #     prev_height = -1
    #     for x, height in enumerate(row[::-1]):
    #         # print([x, y])
    #         # print(height, prev_height)
    #         if height > prev_height:
    #             # print([x, y], height, prev_height)
    #             visible_map[y][len(row) - x - 1] = True
    #             prev_height = height

    # for x in range(len(forest_map[0])):
    #     prev_height = -1
    #     for y in range(len(forest_map)):
    #         # print([x, y])
    #         height = forest_map[y][x]
    #         # print(height, prev_height)
    #         if forest_map[y][x] > prev_height:
    #             visible_map[y][x] = True
    #             prev_height = height

    #     prev_height = -1
    #     for y in range(len(forest_map) - 1, -1, -1):
    #         height = forest_map[y][x]
    #         if forest_map[y][x] > prev_height:
    #             visible_map[y][x] = True
    #             prev_height = height

    return visible_map


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    visible_map = get_tall_trees(inputs)

    return sum([len([visible for visible in row if visible]) for row in visible_map])


def get_scenic_score(forest_map, location):
    x, y = location
    view_distances = []
    current_height = forest_map[y][x]
    score = 1

    for direction in DIRECTIONS:
        this_score = 0
        while True:
            new_position = tuple(map(operator.add, location, tuple(value * (this_score + 1) for value in direction)))
            if min(new_position) < 0 or new_position[0] >= len(forest_map[0]) or new_position[1] >= len(forest_map):
                break
            this_score += 1
            if forest_map[new_position[1]][new_position[0]] >= current_height:
                break
        view_distances.append(this_score)
        score *= this_score

    return score


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    max_scenic_score = 0

    for y in range(len(inputs)):
        for x in range(len(inputs[0])):
            max_scenic_score = max(max_scenic_score, get_scenic_score(inputs, (x, y)))

    return max_scenic_score


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
