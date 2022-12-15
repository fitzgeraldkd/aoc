import json
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.lists import split
from utils.setup import read_inputs


def parse_input(input: str):
    return [json.loads(line.strip()) for line in input]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    grouped = split(read_inputs(script_directory), '\n')
    return [parser(line) for line in grouped]


def is_correct_order(item_1, item_2):
    if isinstance(item_1, list) and isinstance(item_2, list):
        fallback = None if len(item_1) == len(item_2) else len(item_1) < len(item_2)
        for index in range(len(item_1)):
            if index >= len(item_2):
                return False
            result = is_correct_order(item_1[index], item_2[index])
            if result is not None:
                return result
        return fallback
    elif isinstance(item_1, int) and isinstance(item_2, int):
        return None if item_1 == item_2 else item_1 < item_2
    else:
        return is_correct_order(item_1 if isinstance(item_1, list) else [item_1],
                                item_2 if isinstance(item_2, list) else [item_2])


def part_1(override_inputs = None):
    pairs = get_inputs(parse_input) if override_inputs is None else override_inputs
    indeces_sum = 0

    for index, (item_1, item_2) in enumerate(pairs):
        indeces_sum += 1 + index if is_correct_order(item_1, item_2) else 0

    return indeces_sum


def sort(packets):
    sorted_packets = [packets.pop()]
    while packets:
        next_packet = packets.pop()
        for i in range(len(sorted_packets)):
            if is_correct_order(next_packet, sorted_packets[i]):
                sorted_packets.insert(i, next_packet)
                break
            elif i == len(sorted_packets) - 1:
                sorted_packets.append(next_packet)
    return sorted_packets


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    flat_packets = [[[2]], [[6]]]
    for pair in inputs:
        flat_packets.extend(pair)

    sorted_packets = sort(flat_packets)

    return (sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]]) + 1)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
