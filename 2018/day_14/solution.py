import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)][0]


def join_str(recipes, start=None, end=None):
    return ''.join([str(recipe) for recipe in recipes[start:end]])


def part_1(override_inputs = None):
    target_recipes = get_inputs(parse_input) if override_inputs is None else override_inputs

    recipes = [3, 7]
    indeces = [0, 1]

    while len(recipes) < (target_recipes + 10):
        total = recipes[indeces[0]] + recipes[indeces[1]]
        if total >= 10:
            recipes.extend([1, total - 10])
        else:
            recipes.append(total)
        indeces[0] = (indeces[0] + recipes[indeces[0]] + 1) % len(recipes)
        indeces[1] = (indeces[1] + recipes[indeces[1]] + 1) % len(recipes)

    return join_str(recipes, target_recipes, target_recipes + 10)

def part_2(override_inputs = None):
    target_score = get_inputs(parse_input) if override_inputs is None else override_inputs
    target_score = str(target_score)

    recipes = [3, 7]
    indeces = [0, 1]

    while target_score not in join_str(recipes, -1 * (len(target_score) + 2)):
        total = recipes[indeces[0]] + recipes[indeces[1]]
        if total >= 10:
            recipes.extend([1, total - 10])
        else:
            recipes.append(total)
        indeces[0] = (indeces[0] + recipes[indeces[0]] + 1) % len(recipes)
        indeces[1] = (indeces[1] + recipes[indeces[1]] + 1) % len(recipes)

    return len(join_str(recipes).split(target_score)[0])


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
