import os
import re


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()

    return inputs


def part_1():
    inputs = get_inputs()

    sum = 0
    for input in inputs:
        code = len(input)
        memory = code - 2 - len(re.findall(r'(\\\\|\\\")', input)) - 3 * len(re.findall(r'\\x[0-9a-f]{2}', input))
        sum += code - memory

    return sum


def part_2():
    inputs = get_inputs()

    sum = 0
    for input in inputs:
        code = len(input)
        encoded = code + 2 + len(re.findall(r'(\\|\")', input))
        sum += encoded - code

    return sum


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
