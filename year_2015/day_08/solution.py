import re

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def part_1():
    inputs = get_inputs()
    return sum(2 + len(re.findall(r'(\\\\|\\\")', input)) + 3 * len(re.findall(r'\\x[0-9a-f]{2}', input))
               for input in inputs)


def part_2():
    inputs = get_inputs()
    return sum(2 + len(re.findall(r'(\\|\")', input)) for input in inputs)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
