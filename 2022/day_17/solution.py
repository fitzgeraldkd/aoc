import numpy as np
import operator
import os
import sys
from collections import defaultdict
from tqdm import trange
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import get_tqdm_kwargs, read_inputs


ROCKS = [
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(1, 0), (0, -1), (1, -1), (2, -1), (1, -2)],
    [(2, 0), (2, -1), (0, -2), (1, -2), (2, -2)],
    [(0, 0), (0, -1), (0, -2), (0, -3)],
    [(0, 0), (1, 0), (0, -1), (1, -1)]
]


def parse_input(input: str):
    return input.strip()
    return int(input.strip())


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]
    return [parser(line) for line in read_inputs(script_directory, 'sample.txt')][0]


def check_collision(rocks, rock, origin, direction):
    # print(rock, direction)
    positioned_rock = [tuple(map(operator.add, pebble, origin)) for pebble in rock]
    if direction == (-1, 0) and any(pebble[0] == 0 for pebble in positioned_rock):
        return True
    elif direction == (1, 0) and any(pebble[0] == 6 for pebble in positioned_rock):
        return True
    elif direction == (0, -1) and any(pebble[1] == 1 for pebble in positioned_rock):
        return True

    return any([tuple(map(operator.add, pebble, direction)) in rocks for pebble in positioned_rock])


def part_1(override_inputs = None):
    jets = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = None

    rocks = set()
    highest_elevation = 0
    jet_index = 0

    for i in trange(2022, **get_tqdm_kwargs(__file__, 1)):
        rock = ROCKS[i % len(ROCKS)]
        origin = (2, highest_elevation + 4 - min(rock, key=lambda piece: piece[1])[1])
        # print(rocks)
        # input()

        while True:
            # print(origin)
            # input()
            jet = jets[jet_index % len(jets)]
            jet_index += 1
            if not check_collision(rocks, rock, origin, (-1, 0) if jet == '<' else (1, 0)):
                origin = (origin[0] + (-1 if jet == '<' else 1), origin[1])

            if check_collision(rocks, rock, origin, (0, -1)):
                highest_elevation = max(highest_elevation, origin[1])
                # print('origin', origin)
                [rocks.add(tuple(map(operator.add, pebble, origin))) for pebble in rock]
                break
            else:
                origin = (origin[0], origin[1] - 1)

    return highest_elevation


def check_collision_pt2(rocks, rock, origin, direction):
    # print(rock, direction)
    positioned_rock = [tuple(map(operator.add, pebble, origin)) for pebble in rock]
    if direction == (-1, 0) and any(pebble[0] == 0 for pebble in positioned_rock):
        return True
    elif direction == (1, 0) and any(pebble[0] == 6 for pebble in positioned_rock):
        return True
    elif direction == (0, -1) and any(pebble[1] == 1 for pebble in positioned_rock):
        return True

    new_rock = [tuple(map(operator.add, pebble, direction)) for pebble in positioned_rock]
    return any([x in rocks[y] for x, y in new_rock])
    return any([tuple(map(operator.add, pebble, direction)) in rocks for pebble in positioned_rock])


def part_2(override_inputs = None):
    jets = get_inputs(parse_input) if override_inputs is None else override_inputs
    jet_index = 0
    highest_elevation = 0
    rocks = defaultdict(set)
    repeated_pattern = np.lcm(len(jets), len(ROCKS))
    checked_states = {}
    target = 1000000000000
    additional_height = 0
    i = 0

    while i < target:
    # for i in trange(1000000000000):
        # print(len(rocks))
        # print(i, additional_height)
        # if additional_height > 0:
            # print(i)
            # input()
        if i % repeated_pattern == 0 and len(rocks.keys()) >= 100 and additional_height == 0:
            print('Checking...')
            key = []
            for y in range(highest_elevation, highest_elevation - 100, -1):
                row_key = []
                for x in range(7):
                    row_key.append('#' if x in rocks[y] else '.')
                key.append(''.join(row_key))
            key = ''.join(key)
            if key in checked_states:
                print('MATCH FOUND')
                print(checked_states[key], i)
                remaining = target - i
                last_index, last_height = checked_states[key]
                cycles_to_skip = remaining // (i - last_index)
                additional_height = cycles_to_skip * (highest_elevation - last_height)
                print(remaining, cycles_to_skip, additional_height)


                i += cycles_to_skip * (i - last_index)
            else:
                print('No match...', len(checked_states) + 1, 'states checked.')
                checked_states[key] = (i, highest_elevation)
            # key = [['#' for x in range(7) if x in row else '.'] for row in rocks]

        rock = ROCKS[i % len(ROCKS)]
        origin = (2, highest_elevation + 4 - min(rock, key=lambda piece: piece[1])[1])

        while True:
            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)
            if not check_collision_pt2(rocks, rock, origin, (-1, 0) if jet == '<' else (1, 0)):
                origin = (origin[0] + (-1 if jet == '<' else 1), origin[1])

            if check_collision_pt2(rocks, rock, origin, (0, -1)):
                highest_elevation = max(highest_elevation, origin[1])
                # print('origin', origin)
                positioned_rock = [tuple(map(operator.add, pebble, origin)) for pebble in rock]
                # print(positioned_rock)
                for x, y in positioned_rock:
                    rocks[y].add(x)
                # [rocks.add(tuple(map(operator.add, pebble, origin))) for pebble in rock]
                break
            else:
                origin = (origin[0], origin[1] - 1)

        i += 1

    return highest_elevation + additional_height


    # jets = get_inputs(parse_input) if override_inputs is None else override_inputs
    # output = None

    # rocks = set()
    # highest_elevation = 0
    # jet_index = 0

    # repeated_pattern = np.lcm(len(jets), len(ROCKS))
    # last_highest_elevation = 0
    # differences = []
    # previous_states = {}

    # for i in trange(1000000000000, disable=True):
    #     if i != 0 and i % repeated_pattern == 0:
    #         differences.append(highest_elevation - last_highest_elevation)
    #         # print(differences)
    #         print(highest_elevation - last_highest_elevation)
    #         last_highest_elevation = highest_elevation
    #         # input()
    #     rock = ROCKS[i % len(ROCKS)]
    #     origin = (2, highest_elevation + 4 - min(rock, key=lambda piece: piece[1])[1])
    #     # print(rocks)
    #     # input()

    #     while True:
    #         # print(origin)
    #         # input()
    #         jet = jets[jet_index % len(jets)]
    #         jet_index += 1
    #         if not check_collision(rocks, rock, origin, (-1, 0) if jet == '<' else (1, 0)):
    #             origin = (origin[0] + (-1 if jet == '<' else 1), origin[1])

    #         if check_collision(rocks, rock, origin, (0, -1)):
    #             highest_elevation = max(highest_elevation, origin[1])
    #             # print('origin', origin)
    #             [rocks.add(tuple(map(operator.add, pebble, origin))) for pebble in rock]
    #             break
    #         else:
    #             origin = (origin[0], origin[1] - 1)

    # return highest_elevation


if __name__ == '__main__':
    # print('Part 1:', part_1())
    print('Part 2:', part_2())
