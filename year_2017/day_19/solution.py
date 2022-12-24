import operator
import re
from typing import Callable, List, Tuple

from utils.setup import read_inputs


def parse_input(input: str):
    return input
    return f' {input} '


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def parse_map(map: List[str]):
    start = (map[0].index('|'), 0)
    intersections = []
    letters = {}

    for y, row in enumerate(map):
        intersections.extend(([match.start() for match in re.finditer(r'\+', row)], y))
        for match in re.finditer(r'[A-Z]', row):
            letters[match.group(0)] = (match.start(), y)

    return start, intersections, letters

class Map:
    def __init__(self, raw_map: List[str]):
        self.position = (raw_map[0].index('|'), 0)
        self.intersections = []
        self.letters = {}
        self.facing = (0, 1)
        self.at_end = False
        self.raw_map = raw_map
        self.collected_letters = []
        self.distance_traveled = 1

        for y, row in enumerate(raw_map):
            # print([match for match in re.finditer(r'\+', row)])
            self.intersections.extend(([(match.start(), y) for match in re.finditer(r'\+', row)]))
            for match in re.finditer(r'[A-Z]', row):
                self.letters[match.group(0)] = (match.start(), y)

    def get_distance(self, start: Tuple[int, int], end: Tuple[int, int]):
        return abs(start[0] - end[0]) + abs(start[1] - end[1])

    def get_letters_between_points(self, start: Tuple[int, int], end: Tuple[int, int]):
        consistent_axis, varying_axis = (0, 1) if start[0] == end[0] else (1, 0)
        condition = lambda letter: (
            letter[1][consistent_axis] == start[consistent_axis] and
            (
                (letter[1][varying_axis] >= start[varying_axis] and letter[1][varying_axis] <= end[varying_axis]) or
                (letter[1][varying_axis] <= start[varying_axis] and letter[1][varying_axis] >= end[varying_axis])
            )
        )
        return [letter for letter in filter(condition, self.letters.items())]

    def move_to_next_intersection(self):
        consistent_axis, varying_axis = (0, 1) if self.facing[0] == 0 else (1, 0)
        moving_negative = True if self.facing[varying_axis] < 0 else False

        next_intersection = None
        for intersection in self.intersections:
            # Skip if the intersection is not in the line of sight.
            # print(self.intersections)
            # print(intersection, self.position, self.facing)
            if intersection[consistent_axis] != self.position[consistent_axis]:
                continue
            if (intersection[varying_axis] - self.position[varying_axis]) * (-1 if moving_negative else 1) < 0:
                continue
            if intersection[0] == self.position[0] and intersection[1] == self.position[1]:
                continue

            if next_intersection is None or abs(intersection[varying_axis] - self.position[varying_axis]) < abs(next_intersection[varying_axis] - self.position[varying_axis]):
                next_intersection = intersection

        if next_intersection is None:
            check_coordinate = self.position
            while self.raw_map[check_coordinate[1]][check_coordinate[0]] != ' ':
                next_intersection = check_coordinate
                check_coordinate = tuple(map(operator.add, check_coordinate, self.facing))
            self.at_end = True

        collected_letters = self.get_letters_between_points(self.position, next_intersection)
        # self.collected_letters.extend(map(sorted(collected_letters)))
        sorted_letters = sorted(collected_letters, key=lambda letter: self.get_distance(self.position, letter[1]))
        self.collected_letters.extend(letter[0] for letter in sorted_letters)

        self.distance_traveled += self.get_distance(self.position, next_intersection)
        self.position = next_intersection
        if consistent_axis == 0:
            self.facing = (1, 0) if self.raw_map[self.position[1]][self.position[0] + 1] != ' ' else (-1, 0)
        else:
            self.facing = (0, 1) if self.raw_map[self.position[1] + 1][self.position[0]] != ' ' else (0, -1)
        # print(self.position)
        # print(self.facing)
        # input()

def part_1(override_inputs = None):
    raw_map = get_inputs(parse_input) if override_inputs is None else override_inputs

    map_object = Map(raw_map)
    # print(parse_map(map))
    # [print(line[0:10]) for line in map]
    while not map_object.at_end:
        map_object.move_to_next_intersection()


    return ''.join(map_object.collected_letters)


def part_2(override_inputs = None):
    raw_map = get_inputs(parse_input) if override_inputs is None else override_inputs

    map_object = Map(raw_map)
    # print(parse_map(map))
    # [print(line[0:10]) for line in map]
    while not map_object.at_end:
        map_object.move_to_next_intersection()


    return map_object.distance_traveled


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
