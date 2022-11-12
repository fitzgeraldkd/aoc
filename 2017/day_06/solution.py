import os
import re
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def parse_input(input: str):
    return [int(value) for value in re.split(r'\s+', input.strip())]


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def stringify_banks(banks):
    return ','.join(str(value) for value in banks)


def part_1():
    banks = get_inputs()

    checked_states = set()

    cycles = 0
    while stringify_banks(banks) not in checked_states:
        checked_states.add(stringify_banks(banks))

        max_index = max(range(len(banks)), key=banks.__getitem__)
        amount_to_add = banks[max_index] // len(banks)
        extra = banks[max_index] % len(banks)
        banks[max_index] = 0
        for i in range(len(banks)):
            index = (max_index + i + 1) % len(banks)
            banks[index] += amount_to_add + (1 if i < extra else 0)
        
        cycles += 1

    return cycles


def part_2():
    banks = get_inputs()

    checked_states = {}

    cycles = 0
    while stringify_banks(banks) not in checked_states:
        checked_states[stringify_banks(banks)] = cycles

        max_index = max(range(len(banks)), key=banks.__getitem__)
        amount_to_add = banks[max_index] // len(banks)
        extra = banks[max_index] % len(banks)
        banks[max_index] = 0
        for i in range(len(banks)):
            index = (max_index + i + 1) % len(banks)
            banks[index] += amount_to_add + (1 if i < extra else 0)
        
        cycles += 1

    return cycles - checked_states[stringify_banks(banks)]


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())