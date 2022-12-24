import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.LinkedList import DoublyLinkedList
from utils.setup import read_inputs


def parse_input(input: str):
    players, _, _, _, _, _, points, _ = input.strip().split()
    return [int(value) for value in [players, points]]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)][0]


def get_max_score(players: int, points: int):
    scores = [0 for _ in range(players)]
    current_player = 0
    current_marble = DoublyLinkedList(0, close_loop=True)

    for next_marble in range(1, points + 1):
        if next_marble % 23 == 0:
            current_marble = current_marble.prev.prev.prev.prev.prev.prev
            scores[current_player] += next_marble + current_marble.prev.remove()
        else:
            current_marble = current_marble.next.append(next_marble)
        current_player = (current_player + 1) % players

    return max(scores)


def part_1(override_inputs = None):
    players, points = get_inputs(parse_input) if override_inputs is None else override_inputs
    return get_max_score(players, points)


def part_2(override_inputs = None):
    players, points = get_inputs(parse_input) if override_inputs is None else override_inputs
    return get_max_score(players, points * 100)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
