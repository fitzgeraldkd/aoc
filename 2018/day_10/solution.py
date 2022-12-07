import os
import re
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


MAX_CHARACTER_HEIGHT = 20


def parse_input(input: str):
    return [[int(value) for value in match[1:-1].split(',')]
        for match in re.findall(r'<\s*-?\d+,\s*-?\d+>', input.strip())]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def get_sky(stars):
    min_x = min(stars, key=lambda star: star[0][0])[0][0]
    max_x = max(stars, key=lambda star: star[0][0])[0][0]
    min_y = min(stars, key=lambda star: star[0][1])[0][1]
    max_y = max(stars, key=lambda star: star[0][1])[0][1]

    sky = [['.' for _ in range(1 + max_x - min_x)] for _ in range(1 + max_y - min_y)]
    print(min_x, max_x, min_y, max_y)

    for star in stars:
        sky[star[0][1] - min_y][star[0][0] - min_x] = '#'

    return sky

    for row in sky:
        print(''.join(row))


def part_1(override_inputs = None):
    stars = get_inputs(parse_input) if override_inputs is None else override_inputs

    north_star = max(stars, key=lambda star: star[0][1])
    south_star = min(stars, key=lambda star: star[0][1])
    seconds_to_skip = ((north_star[0][1] - south_star[0][1] - MAX_CHARACTER_HEIGHT) // (south_star[1][1] - north_star[1][1]))

    for star in stars:
        star[0][0] += star[1][0] * seconds_to_skip
        star[0][1] += star[1][1] * seconds_to_skip

    while (max(stars, key=lambda star: star[0][1])[0][1] -  min(stars, key=lambda star: star[0][1])[0][1]) <= MAX_CHARACTER_HEIGHT + 15:
        for star in stars:
            star[0][0] += star[1][0]
            star[0][1] += star[1][1]

        # print(max(stars, key=lambda star: star[0][1])[0][1],  min(stars, key=lambda star: star[0][1])[0][1])

        sky = get_sky(stars)

        for row in sky:
            print(''.join(row))
    return sky


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
