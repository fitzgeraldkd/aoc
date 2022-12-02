import operator
import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


INFECTED_TURN = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1)
}


CLEAN_TURN = {
    (0, -1): (-1, 0),
    (-1, 0): (0, 1),
    (0, 1): (1, 0),
    (1, 0): (0, -1)
}


FLAGGED_TURN = {
    (0, -1): (0, 1),
    (0, 1): (0, -1),
    (-1, 0): (1, 0),
    (1, 0): (-1, 0)
}


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    state = defaultdict(lambda: '.')
    position = (len(inputs[0]) // 2, len(inputs) // 2)
    facing = (0, -1)

    for y, row in enumerate(inputs):
        for x, cell in enumerate(row):
            if cell == '#':
                state[(x, y)] = '#'

    times_infection_added = 0

    for _ in range(10000):
        if state[position] == '.':
            state[position] = '#'
            facing = CLEAN_TURN[facing]
            times_infection_added += 1
        else:
            state[position] = '.'
            facing = INFECTED_TURN[facing]
        position = tuple(map(operator.add, position, facing))
        
    return times_infection_added


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    state = defaultdict(lambda: '.')
    position = (len(inputs[0]) // 2, len(inputs) // 2)
    facing = (0, -1)

    for y, row in enumerate(inputs):
        for x, cell in enumerate(row):
            if cell == '#':
                state[(x, y)] = '#'

    times_infection_added = 0

    for _ in range(10000000):
        if state[position] == '.':
            state[position] = 'W'
            facing = CLEAN_TURN[facing]
        elif state[position] == '#':
            state[position] = 'F'
            facing = INFECTED_TURN[facing]
        elif state[position] == 'F':
            state[position] = '.'
            facing = FLAGGED_TURN[facing]
        else:
            state[position] = '#'
            times_infection_added += 1
        position = tuple(map(operator.add, position, facing))
        
    return times_infection_added


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())