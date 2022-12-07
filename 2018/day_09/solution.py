import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    players, _, _, _, _, _, points, _ = input.strip().split()
    return [int(value) for value in [players, points]]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]


def part_1(override_inputs = None):
    players, points = get_inputs(parse_input) if override_inputs is None else override_inputs

    scores = [0 for _ in range(players)]
    current_player = 0
    next_marble = 1
    current_index = 0
    marbles = [0]
    while next_marble < points:
        if next_marble % 23 == 0:
            index_to_pop = (current_index - 7) % len(marbles)
            scores[current_player] += next_marble + marbles.pop(index_to_pop)
            current_index = index_to_pop % len(marbles)
        else:
            new_index = (current_index + 2) % len(marbles)
            marbles.insert(new_index, next_marble)
            current_index = new_index

        next_marble += 1
        current_player = (current_player + 1) % players

    return max(scores)


def part_2(override_inputs = None):
    # TODO: Does not solve in a reasonable time.
    return None
    players, points = get_inputs(parse_input) if override_inputs is None else override_inputs
    points *= 100

    scores = [0 for _ in range(players)]
    current_player = 0
    next_marble = 1
    current_index = 0
    marbles = [0]
    while next_marble < points:
        if next_marble % 23 == 0:
            index_to_pop = (current_index - 7) % len(marbles)
            scores[current_player] += next_marble + marbles.pop(index_to_pop)
            current_index = index_to_pop % len(marbles)
        else:
            new_index = (current_index + 2) % len(marbles)
            marbles.insert(new_index, next_marble)
            current_index = new_index

        next_marble += 1
        current_player = (current_player + 1) % players

    return max(scores)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
