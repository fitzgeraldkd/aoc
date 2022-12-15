import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import get_manhattan_distance
from utils.setup import read_inputs


PART_1_TARGET_ROW = 2000000
PART_2_MAX_COORDINATE = 4000000

def parse_input(input: str):
    _, _, sensor_x, sensor_y, _, _, _, _, beacon_x, beacon_y = input.strip().split()
    [sensor_x, sensor_y, beacon_x, beacon_y] = [int(value[:-1].split('=')[-1]) for value in
                                                [sensor_x, sensor_y, beacon_x, f'{beacon_y}_']]
    return [(sensor_x, sensor_y), (beacon_x, beacon_y)]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


# def get_blocked_row(pairs, target_row):
#     blocked_x_values = set()

#     for sensor, beacon in pairs:
#         distance_to_beacon = get_manhattan_distance(sensor, beacon)
#         distance_to_target_row = abs(sensor[1] - target_row)
#         if distance_to_beacon >= distance_to_target_row:
#             x_offset = distance_to_beacon - distance_to_target_row
#             # print(sensor, beacon, x_offset)
#             [blocked_x_values.add(x) for x in range(sensor[0] - x_offset, sensor[0] + x_offset + 1)]

#     for _, beacon in pairs:
#         if beacon[1] == target_row:
#             blocked_x_values.discard(beacon[0])

#     return blocked_x_values



def part_1(override_inputs = None):
    pairs = get_inputs(parse_input) if override_inputs is None else override_inputs

    blocked_x_values = set()

    for sensor, beacon in pairs:
        x_offset = get_manhattan_distance(sensor, beacon) - abs(sensor[1] - PART_1_TARGET_ROW)
        if x_offset >= 0:
            [blocked_x_values.add(x) for x in range(sensor[0] - x_offset, sensor[0] + x_offset + 1)]

    for _, beacon in pairs:
        if beacon[1] == PART_1_TARGET_ROW:
            blocked_x_values.discard(beacon[0])

    return len(blocked_x_values)


def is_in_range(sensor, beacon, point):
    return get_manhattan_distance(sensor, point) <= get_manhattan_distance(sensor, beacon)


def part_2(override_inputs = None):
    pairs = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = None

    mapped_beacons = defaultdict(list)

    for sensor, beacon in pairs:
        distance = get_manhattan_distance(sensor, beacon)
        for y in range(sensor[1] - distance, sensor[1] + distance + 1):
            mapped_beacons[y].append((sensor, beacon))

    x, y = 0, 0
    while y <= PART_2_MAX_COORDINATE:
        sensor, beacon = next(((sensor, beacon) for sensor, beacon in mapped_beacons[y]
                               if is_in_range(sensor, beacon, (x, y))), (None, None))

        if sensor is None:
            return x * 4000000 + y

        delta_x = sensor[0] - x

        if delta_x >= 0:
            x += 2 * (sensor[0] - x) + 1
        else:
            x += get_manhattan_distance(sensor, beacon) - get_manhattan_distance(sensor, (x, y)) + 1

        if x > PART_2_MAX_COORDINATE:
            x = 0
            y += 1

    return output


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
