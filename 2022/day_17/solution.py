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


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]


def check_collision(rocks, rock, origin, direction):
    positioned_rock = [tuple(map(operator.add, pebble, origin)) for pebble in rock]
    if direction == (-1, 0) and any(pebble[0] == 0 for pebble in positioned_rock):
        return True
    elif direction == (1, 0) and any(pebble[0] == 6 for pebble in positioned_rock):
        return True
    elif direction == (0, -1) and any(pebble[1] == 1 for pebble in positioned_rock):
        return True

    return any([x in rocks[y] for x, y in [tuple(map(operator.add, pebble, direction)) for pebble in positioned_rock]])


def part_1(override_inputs = None):
    jets = get_inputs(parse_input) if override_inputs is None else override_inputs

    rocks = defaultdict(set)
    highest_elevation = 0
    jet_index = 0

    for i in trange(2022, **get_tqdm_kwargs(__file__, 1)):
        rock = ROCKS[i % len(ROCKS)]
        origin = (2, highest_elevation + 4 - min(rock, key=lambda piece: piece[1])[1])

        while True:
            jet = jets[jet_index % len(jets)]
            jet_index += 1
            if not check_collision(rocks, rock, origin, (-1, 0) if jet == '<' else (1, 0)):
                origin = (origin[0] + (-1 if jet == '<' else 1), origin[1])

            if check_collision(rocks, rock, origin, (0, -1)):
                highest_elevation = max(highest_elevation, origin[1])
                for x, y in [tuple(map(operator.add, pebble, origin)) for pebble in rock]:
                    rocks[y].add(x)
                break
            else:
                origin = (origin[0], origin[1] - 1)

    return highest_elevation


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
        if i % repeated_pattern == 0 and len(rocks.keys()) >= 100 and additional_height == 0:
            key = []
            for y in range(highest_elevation, highest_elevation - 100, -1):
                row_key = []
                for x in range(7):
                    row_key.append('#' if x in rocks[y] else '.')
                key.append(''.join(row_key))
            key = ''.join(key)
            if key in checked_states:
                remaining = target - i
                last_index, last_height = checked_states[key]
                cycles_to_skip = remaining // (i - last_index)
                additional_height = cycles_to_skip * (highest_elevation - last_height)
                i += cycles_to_skip * (i - last_index)
            else:
                checked_states[key] = (i, highest_elevation)

        rock = ROCKS[i % len(ROCKS)]
        origin = (2, highest_elevation + 4 - min(rock, key=lambda piece: piece[1])[1])

        while True:
            jet = jets[jet_index]
            jet_index = (jet_index + 1) % len(jets)
            if not check_collision(rocks, rock, origin, (-1, 0) if jet == '<' else (1, 0)):
                origin = (origin[0] + (-1 if jet == '<' else 1), origin[1])

            if check_collision(rocks, rock, origin, (0, -1)):
                highest_elevation = max(highest_elevation, origin[1])
                positioned_rock = [tuple(map(operator.add, pebble, origin)) for pebble in rock]
                for x, y in positioned_rock:
                    rocks[y].add(x)
                break
            else:
                origin = (origin[0], origin[1] - 1)

        i += 1

    return highest_elevation + additional_height


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
