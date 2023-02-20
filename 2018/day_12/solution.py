import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.lists import split
from utils.setup import read_inputs


def get_inputs():
    initial_state, notes = split(read_inputs(__file__), '\n')
    notes = [note.strip().split(' => ') for note in notes]
    plants = { index for index, item in enumerate(initial_state[0].strip().split(': ')[1]) if item == '#' }
    notes = { pattern: output for pattern, output in notes }
    return plants, notes


def get_key(plants, index: int):
    return ''.join([('#' if i in plants else '.') for i in range(index - 2, index + 3)])


def run_generations(plants: set, notes: dict, generations: int):
    min_index = min(plants) - 2
    max_index = max(plants) + 2
    differences = [None for _ in range(5)]

    for generation in range(generations):
        new_plants = set()
        for index in range(min_index, max_index + 1):
            if notes.get(get_key(plants, index), '.') == '#':
                new_plants.add(index)
                min_index = min(min_index, index - 2)
                max_index = max(max_index, index + 2)

        differences.pop(0)
        differences.append(sum(new_plants) - sum(plants))

        # Eventually the sum of the plants will continue growing at a constant rate.
        if all([difference is not None for difference in differences]) \
            and len(set(differences)) == 1:
            return sum(plants) + (generations - generation) * differences[0]

        plants = new_plants

    return sum(plants)


def part_1(override_inputs = None):
    plants, notes = get_inputs() if override_inputs is None else override_inputs
    return run_generations(plants, notes, generations=20)


def part_2(override_inputs = None):
    plants, notes = get_inputs() if override_inputs is None else override_inputs
    return run_generations(plants, notes, generations=50000000000)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
