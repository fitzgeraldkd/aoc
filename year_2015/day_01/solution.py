from utils.setup import read_inputs


def get_inputs():
    return [line.strip() for line in read_inputs(__file__)][0]


def part_1(override_inputs: str = None):
    inputs = override_inputs or get_inputs()
    current_floor = 0
    for input in inputs:
        current_floor += 1 if input == '(' else -1
    return current_floor


def part_2(override_inputs: str = None):
    inputs = override_inputs or get_inputs()
    current_floor = 0
    for index, input in enumerate(inputs):
        current_floor += 1 if input == '(' else -1
        if current_floor < 0:
            return index + 1


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
