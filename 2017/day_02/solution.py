import os
import re
import sys
from typing import List

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def parse_input(input: str):
    return [int(cell) for cell in re.split(r'\s+', input.strip())]


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1(override_inputs: List[List[int]] = None):
    spreadsheet = get_inputs() if override_inputs is None else override_inputs
    total = 0

    for row in spreadsheet:
        total += max(row) - min(row)

    return total


def get_row_result(row: List[int]):
    sorted_row = sorted(row)
    while len(sorted_row) > 0:
        dividend = sorted_row.pop()
        for divisor in sorted_row:
            if dividend % divisor == 0:
                return int(dividend / divisor)
            if divisor > dividend / 2:
                break


def part_2(override_inputs: List[List[int]] = None):
    spreadsheet = get_inputs() if override_inputs is None else override_inputs
    total = 0

    for row in spreadsheet:
        total += get_row_result(row)

    return total


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
