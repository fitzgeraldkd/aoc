import os
import sys
from collections import Counter
from itertools import combinations
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    ids = get_inputs(parse_input) if override_inputs is None else override_inputs
    counted_ids = [Counter(id).items() for id in ids]

    two_characters = len([id for id in counted_ids if any(count == 2 for _, count in id)])
    three_characters = len([id for id in counted_ids if any(count == 3 for _, count in id)])

    return two_characters * three_characters


def part_2(override_inputs = None):
    ids = get_inputs(parse_input) if override_inputs is None else override_inputs

    ids_with_count = [{'id': id, 'count': Counter(id)} for id in ids]
    pairs = combinations(ids_with_count, 2)

    for pair in pairs:
        if sum((pair[0]['count'] - pair[1]['count']).values()) == 1:
            unmatched_index = None
            for index in range(len(pair[0]['id'])):
                if pair[0]['id'][index] != pair[1]['id'][index]:
                    if unmatched_index is None:
                        unmatched_index = index
                    else:
                        break
                if index == len(pair[0]['id']) - 1:
                    return pair[0]['id'][:unmatched_index] + pair[0]['id'][unmatched_index + 1:]


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
