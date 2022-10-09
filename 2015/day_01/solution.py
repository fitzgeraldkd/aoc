import os


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = file.read()
    file.close()
    return inputs


def part_1():
    inputs = get_inputs()
    current_floor = 0
    for input in inputs:
        current_floor += 1 if input == '(' else -1
    return current_floor


def part_2():
    inputs = get_inputs()
    current_floor = 0
    for index, input in enumerate(inputs):
        current_floor += 1 if input == '(' else -1
        if current_floor < 0:
            return index + 1
    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
