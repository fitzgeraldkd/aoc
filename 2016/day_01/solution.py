import os

X_DIRECTIONS = ['E', 'W']
Y_DIRECTIONS = ['N', 'S']

POSITIVE_DIRECTIONS = ['N', 'E']
NEGATIVE_DIRECTIONS = ['S', 'W']

DIRECTION_MAP = {
    'N': {
        'L': 'W',
        'R': 'E'
    },
    'E': {
        'L': 'N',
        'R': 'S'
    },
    'S': {
        'L': 'E',
        'R': 'W'
    },
    'W': {
        'L': 'S',
        'R': 'N'
    }
}


def parse_input(input: str):
    return input.strip().split(', ')


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def part_1():
    inputs = get_inputs()

    direction = 'N'
    x = 0
    y = 0

    for input in inputs:
        direction = DIRECTION_MAP[direction][input[0]]
        distance = int(input[1:]) * (1 if direction in POSITIVE_DIRECTIONS else -1)
        if direction in X_DIRECTIONS:
            x += distance
        else:
            y += distance

    return x + y


def part_2():
    inputs = get_inputs()

    direction = 'N'
    x = 0
    y = 0

    locations = {}


    for input in inputs:
        direction = DIRECTION_MAP[direction][input[0]]
        distance = int(input[1:])

        for _ in range(distance):
            delta = 1 if direction in POSITIVE_DIRECTIONS else -1
            if direction in X_DIRECTIONS:
                x += delta
            else:
                y += delta

            if x in locations:
                if y in locations[x]:
                    return x + y
                else:
                    locations[x].add(y)
            else:
                locations[x] = { y }


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
