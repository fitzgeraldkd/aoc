import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def parse_input(input: str):
    return int(input.strip())


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def part_1():
    elves = list(range(get_inputs()))

    while len(elves) > 1:
        start = 0 if len(elves) % 2 == 0 else 2
        elves = elves[start::2]

    return elves[0] + 1


def part_2():
    elves = list(range(get_inputs()))

    index = len(elves) // 2
    while len(elves) > 1:
        elves.pop(index)
        if len(elves) % 2 == 0:
            index += 1
        index = index % len(elves)

    return elves[0] + 1


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
