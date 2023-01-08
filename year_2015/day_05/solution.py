import re
from typing import List

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def part_1(override_inputs: List[str] = None):
    inputs = override_inputs or get_inputs()

    nice_string_count = 0
    for input in inputs:
        if re.search(r'(ab|cd|pq|xy)', input):
            continue
        if len(re.findall(r'[aeiou]', input)) < 3:
            continue
        if re.search(r'([a-z])\1', input) is None:
            continue

        nice_string_count += 1

    return nice_string_count


def part_2(override_inputs: List[str] = None):
    inputs = override_inputs or get_inputs()

    nice_string_count = 0
    for input in inputs:

        has_two_pairs = False
        for index in range(len(input) - 3):
            pair = input[index:index+2]
            if re.search(pair, input[index+2:]):
                has_two_pairs = True
                break
        if not has_two_pairs:
            continue

        if re.search(r'([a-z])[a-z]\1', input) is None:
            continue

        nice_string_count += 1

    return nice_string_count


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
