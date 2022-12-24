import math
import numpy as np
import operator
import os
import sys
from tqdm import tqdm
from typing import Callable, Tuple

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue
from utils.pathing import get_adjacent, get_manhattan_distance
from utils.setup import read_inputs

DIRECTION_MAP = {
    '<': (-1, 0),
    '>': (1, 0),
    '^': (0, -1),
    'v': (0, 1)
}

def parse_input(input: str):
    return input.strip()
    return int(input.strip())


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]
    return [parser(line) for line in read_inputs(script_directory, 'sample.txt')]


def move_blizzards(blizzards, boundaries):
    new_blizzards = {
        '<': set(),
        '>': set(),
        '^': set(),
        'v': set()
    }
    # print(boundaries)
    for direction in '<>^v':
        for blizzard in blizzards[direction]:
            new_position = tuple(map(operator.add, blizzard, DIRECTION_MAP[direction]))
            if new_position[0] == boundaries[0][0]:
                new_position = (boundaries[1][0] - 2, new_position[1])
            elif new_position[0] == boundaries[1][0] - 1:
                new_position = (boundaries[0][0] + 1, new_position[1])
            elif new_position[1] == boundaries[0][1]:
                new_position = (new_position[0], boundaries[1][1] - 2)
            elif new_position[1] == boundaries[1][1] - 1:
                new_position = (new_position[0], boundaries[0][1] + 1)
            new_blizzards[direction].add(new_position)
    return new_blizzards


def a_star(start: Tuple[Tuple[int, int], dict], goal: Tuple[int, int], get_is_wall, get_heuristic, progress=None):
    queue = PriorityQueue()
    previous = {}
    g_score = { start: 0 }
    f_score = { start: get_heuristic(start[0], goal) }
    queue.add_item(start, f_score[start])

    while not queue.is_empty():
        current, t = queue.pop()
        # print(current, t, goal)

        if current == goal:
            # print(previous)
            # return t
            path = []
            node = (current, t)
            while node != start:
                path.append(node)
                node = previous[node]
            path.append(start)
            return path

        for neighbor in [current, *get_adjacent(current)]:
            # print(neighbor)
            if get_is_wall(neighbor, t + 1):
                continue
            neighbor_key = (neighbor, t + 1)
            if neighbor_key in previous:
                continue
            neighbor_g_score = g_score[(current, t)] + 1
            if neighbor_g_score < g_score.get(neighbor, math.inf):
                previous[neighbor_key] = (current, t)
                g_score[neighbor_key] = neighbor_g_score
                f_score[neighbor_key] = neighbor_g_score + get_heuristic(neighbor, goal)
                if queue.has_item(neighbor_key):
                    queue.update_priority(neighbor_key, f_score[neighbor_key])
                else:
                    queue.add_item(neighbor_key, f_score[neighbor_key])

        if progress is not None:
            progress.update()

def part_1(override_inputs = None):
    layout = get_inputs(parse_input) if override_inputs is None else override_inputs
    blizzards = {
        0: {
            '<': set(),
            '>': set(),
            '^': set(),
            'v': set()
        }
    }

    walls = { (1, -1) }
    for y, row in enumerate(layout):
        for x, value in enumerate(row):
            if value in '<>^v':
                blizzards[0][value].add((x, y))
            elif value == '#':
                walls.add((x, y))

    boundaries = ((0, 0), (len(layout[0]), len(layout)))
    blizzard_permutations = np.lcm(boundaries[1][0] - 2, boundaries[1][1] - 2)
    for i in range(1, blizzard_permutations):
        blizzards[i] = move_blizzards(blizzards[i - 1], boundaries)

    condensed_blizzards = {}

    for blizzard in blizzards:
        condensed_blizzards[blizzard] = set()
        for direction in '<>^v':
            condensed_blizzards[blizzard] |= blizzards[blizzard][direction]

    # print(condensed_blizzards)
    # for t, blizzard in condensed_blizzards.items():
    #     print(t)
    #     print(blizzard)
    # print(blizzard_permutations)

    # for t, blizzard in condensed_blizzards.items():
    #     print()
    #     print(t)
    #     for i in range(1, boundaries[1][1]):
    #         row = [('#' if (x, i) in blizzard else '.') for x in range(1, boundaries[1][0])]
    #         print(''.join(row))
    #     input()

    position = (1, 0)
    goal = (len(layout[0]) - 2, len(layout) - 1)

    get_is_wall = lambda location, t: location in condensed_blizzards[t % blizzard_permutations] | walls

    path = a_star((position, 0), goal, get_is_wall, get_manhattan_distance)
    # print(path)

    # for location, t in path:
    #     if location in condensed_blizzards[t % blizzard_permutations]:
    #         print('error')

    return len(path) - 1


def part_2(override_inputs = None):
    layout = get_inputs(parse_input) if override_inputs is None else override_inputs
    blizzards = {
        0: {
            '<': set(),
            '>': set(),
            '^': set(),
            'v': set()
        }
    }

    walls = { (1, -1) }
    for y, row in enumerate(layout):
        for x, value in enumerate(row):
            if value in '<>^v':
                blizzards[0][value].add((x, y))
            elif value == '#':
                walls.add((x, y))

    boundaries = ((0, 0), (len(layout[0]), len(layout)))
    blizzard_permutations = np.lcm(boundaries[1][0] - 2, boundaries[1][1] - 2)
    for i in range(1, blizzard_permutations):
        blizzards[i] = move_blizzards(blizzards[i - 1], boundaries)

    condensed_blizzards = {}

    for blizzard in blizzards:
        condensed_blizzards[blizzard] = set()
        for direction in '<>^v':
            condensed_blizzards[blizzard] |= blizzards[blizzard][direction]


    start = (1, 0)
    goal = (len(layout[0]) - 2, len(layout) - 1)
    walls.add((goal[0], goal[1] + 1))

    get_is_wall = lambda location, t: location in condensed_blizzards[t % blizzard_permutations] | walls

    path_1 = a_star((start, 0), goal, get_is_wall, get_manhattan_distance)
    print(len(path_1) - 1)
    path_2 = a_star((goal, len(path_1) - 1), start, get_is_wall, get_manhattan_distance)
    # path_2 = a_star((goal, 245), start, get_is_wall, get_manhattan_distance)
    print(len(path_2) - 1)
    path_3 = a_star((start, len(path_1) + len(path_2) - 2), goal, get_is_wall, get_manhattan_distance)
    # path_3 = a_star((start, 245 + len(path_2) - 1), goal, get_is_wall, get_manhattan_distance)
    print(len(path_3) - 1)



    return len(path_1) + len(path_2) + len(path_3) - 3


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
