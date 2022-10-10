import json
import os
import re


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def part_1():
    inputs = get_inputs()

    numbers = re.findall(r'\-?\d+', inputs)
    total = sum([int(number) for number in numbers])

    return total


def sum_children(data):
    total = 0

    def read_child(child):
        if type(child) is int:
            return child
        elif type(child) is dict or type(child) is list:
            return sum_children(child)
        return 0

    if type(data) is dict:
        if any([value == 'red' for value in data.values()]):
            return total
        
        for value in data.values():
            total += read_child(value)

    elif type(data) is list:
        for value in data:
            total += read_child(value)

    return total


def part_2():
    inputs = get_inputs()

    parsed_input = json.loads(inputs)

    return sum_children(parsed_input)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
