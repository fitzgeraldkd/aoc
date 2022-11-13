import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def part_1(override_inputs: str = None):
    sequence = get_inputs() if override_inputs is None else override_inputs
    sequence = f'{sequence}{sequence[0]}'
    total = 0
    for index in range(len(sequence) - 1):
        if sequence[index] == sequence[index + 1]:
            total += int(sequence[index])
    return total


def part_2(override_inputs: str = None):
    sequence = get_inputs() if override_inputs is None else override_inputs
    total = 0

    for index in range(len(sequence)):
        opposite_index = int(index + len(sequence) / 2) % len(sequence)
        if sequence[index] == sequence[opposite_index]:
            total += int(sequence[index])

    return total


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
