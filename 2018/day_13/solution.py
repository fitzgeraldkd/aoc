import operator
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import rotate
from utils.setup import read_inputs


DIRECTION_MAP = {
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
    '^': (0, -1)
}

INTERSECTION_ROTATIONS = {
    0: 'L',
    1: None,
    2: 'R'
}

def parse_input(input: str):
    return input.replace('\n', '')


def get_inputs(parser: Callable):
    map = [parser(line) for line in read_inputs(__file__)]
    carts = []
    forward_curves = set()
    backward_curves = set()
    intersections = set()
    for y, row in enumerate(map):
        for x, cell in enumerate(row):
            if cell in ['<', '>', 'v', '^']:
                carts.append({
                    'direction': DIRECTION_MAP[cell],
                    'intersections': 0,
                    'position': (x, y),
                })
            elif cell == '/':
                forward_curves.add((x, y))
            elif cell == '\\':
                backward_curves.add((x, y))
            elif cell == '+':
                intersections.add((x, y))
    return carts, forward_curves, backward_curves, intersections


def get_new_position_and_direction(cart, forward_curves, backward_curves, intersections):
        new_position = tuple(map(operator.add, cart['position'], cart['direction']))

        rotation = None
        if new_position in forward_curves:
            rotation = 'R' if cart['direction'][0] == 0 else 'L'
        elif new_position in backward_curves:
            rotation = 'L' if cart['direction'][0] == 0 else 'R'
        elif new_position in intersections:
            rotation = INTERSECTION_ROTATIONS[cart['intersections']]
            cart['intersections'] = (cart['intersections'] + 1) % 3
        new_direction = rotate(cart['direction'], rotation) if rotation else cart['direction']

        return new_position, new_direction


def part_1(override_inputs = None):
    carts, forward_curves, backward_curves, intersections = get_inputs(parse_input) if override_inputs is None else override_inputs
    occupied_positions = set(cart['position'] for cart in carts)

    while True:
        carts = sorted(carts, key=lambda cart: cart['position'][::-1])
        for cart in carts:
            new_position, new_direction = get_new_position_and_direction(cart, forward_curves, backward_curves, intersections)
            if new_position in occupied_positions:
                return f'{new_position[0]},{new_position[1]}'

            occupied_positions.discard(cart['position'])
            occupied_positions.add(new_position)
            cart['position'] = new_position
            cart['direction'] = new_direction


def part_2(override_inputs = None):
    carts, forward_curves, backward_curves, intersections = get_inputs(parse_input) if override_inputs is None else override_inputs
    occupied_positions = set(cart['position'] for cart in carts)
    for cart in carts:
        cart['is_active'] = True

    while True:
        carts = sorted([cart for cart in carts if cart['is_active']], key=lambda cart: cart['position'][::-1])
        for cart in carts:
            if not cart['is_active']:
                continue

            new_position, new_direction = get_new_position_and_direction(cart, forward_curves, backward_curves, intersections)
            if len(occupied_positions) == 1:
                return f'{new_position[0]},{new_position[1]}'

            if new_position in occupied_positions:
                occupied_positions.discard(cart['position'])
                occupied_positions.discard(new_position)
                cart['is_active'] = False
                for other_cart in carts:
                    if other_cart['position'] == new_position:
                        other_cart['is_active'] = False
                continue

            occupied_positions.discard(cart['position'])
            occupied_positions.add(new_position)
            cart['position'] = new_position
            cart['direction'] = new_direction


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
