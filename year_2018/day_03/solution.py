import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    id, _, coords, size = input.strip().split()
    return {
        'id': int(id[1:]),
        'coords': tuple(int(coord) for coord in coords[:-1].split(',')),
        'size': tuple(int(dimension) for dimension in size.split('x'))
    }


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def part_1(override_inputs = None):
    claims = get_inputs(parse_input) if override_inputs is None else override_inputs

    fabric = defaultdict(int)
    for claim in claims:
        for x in range(claim['size'][0]):
            for y in range(claim['size'][1]):
                fabric[(claim['coords'][0] + x, claim['coords'][1] + y)] += 1

    return len([square for square in fabric.values() if square > 1])


def part_2(override_inputs = None):
    claims = get_inputs(parse_input) if override_inputs is None else override_inputs
    non_overlapping = set(claim['id'] for claim in claims)

    fabric = {}
    for claim in claims:
        for x in range(claim['size'][0]):
            for y in range(claim['size'][1]):
                coord = (claim['coords'][0] + x, claim['coords'][1] + y)
                if coord in fabric:
                    non_overlapping.discard(claim['id'])
                    non_overlapping.discard(fabric[coord])
                else:
                    fabric[coord] = claim['id']

    return non_overlapping.pop()


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
