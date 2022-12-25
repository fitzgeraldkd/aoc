import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


SNAFU_MAP = {
    -2: '=',
    -1: '-',
    0: '0',
    1: '1',
    2: '2'
}


SNAFU_DECIMAL_MAP = {
    '=': -2,
    '-': -1,
    '0': 0,
    '1': 1,
    '2': 2
}


def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def snafu_to_decimal(snafu: str):
    return sum(SNAFU_DECIMAL_MAP[char] * (5 ** (digit)) for digit, char in enumerate(snafu[::-1]))


def decimal_to_snafu(decimal: int):
    digits = []
    while True:
        digits.append(decimal % 5)
        decimal //= 5
        if decimal == 0:
            break

    for digit in range(len(digits)):
        if digits[digit] > 2:
            digits[digit] -= 5
            if digit + 1 < len(digits):
                digits[digit + 1] += 1
            else:
                digits.append(1)

    return ''.join(SNAFU_MAP[value] for value in digits[::-1])


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    return decimal_to_snafu(sum(snafu_to_decimal(snafu) for snafu in inputs))


def part_2(override_inputs = None):
    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
