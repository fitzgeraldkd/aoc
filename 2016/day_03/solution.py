import os
import re


def parse_input(input: str):
    return list(map(lambda x: int(x), re.split(r'\s+', input.strip())))


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    inputs = get_inputs()

    possible_triangles = 0
    for input in inputs:
        [x, y, z] = sorted(input)
        if x + y > z:
            possible_triangles += 1

    return possible_triangles


def part_2():
    inputs = get_inputs()

    possible_triangles = 0
    starting_row = 0
    while starting_row < len(inputs) - 1:
        for i in range(3):
            sides = []
            for j in range(3):
                sides.append(inputs[starting_row + j][i])
            [x, y, z] = sorted(sides)
            if x + y > z:
                possible_triangles += 1
        starting_row += 3

    return possible_triangles


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
