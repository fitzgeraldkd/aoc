import itertools
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def get_inputs():
    raw_calorie_list = [line.strip() for line in read_inputs(__file__)]
    grouped_calorie_list = [list(y) for x, y in itertools.groupby(raw_calorie_list, lambda value: value == '') if not x]
    converted_calorie_list = [sum(int(calorie) for calorie in elf) for elf in grouped_calorie_list]
    return converted_calorie_list


def part_1(override_inputs = None):
    elves = get_inputs() if override_inputs is None else override_inputs
    return max(elves)


def part_2(override_inputs = None):
    elves = get_inputs() if override_inputs is None else override_inputs
    return sum(sorted(elves, reverse=True)[:3])


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
