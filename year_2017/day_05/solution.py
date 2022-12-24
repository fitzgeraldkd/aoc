from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def part_1():
    inputs = get_inputs()
    index = 0
    steps = 0

    while index >= 0 and index < len(inputs):
        jump = inputs[index]
        inputs[index] += 1
        index += jump
        steps += 1

    return steps


def part_2():
    inputs = get_inputs()
    index = 0
    steps = 0

    while index >= 0 and index < len(inputs):
        jump = inputs[index]
        inputs[index] += 1 if jump < 3 else -1
        index += jump
        steps += 1

    return steps


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
