import os


DIRECTION_MAP = {
    '^': { 'x': 0, 'y': 1 },
    'v': { 'x': 0, 'y': -1 },
    '>': { 'x': 1, 'y': 0 },
    '<': { 'x': -1, 'y': 0 }
}


def parse_input(input):
    return input


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    inputs = get_inputs()[0]

    x = 0
    y = 0

    houses = { '0,0': 1 }

    for input in inputs:
        delta = DIRECTION_MAP[input]
        x += delta['x']
        y += delta['y']
        key = f'{x},{y}'
        if key in houses:
            houses[key] += 1
        else:
            houses[key] = 1

    return len(houses.keys())


def part_2():
    inputs = get_inputs()[0]

    position_map = {
        'santa': { 'x': 0, 'y': 0 },
        'robo-santa': { 'x': 0, 'y': 0 }
    }

    is_santas_turn = True

    houses = { '0,0': 1 }

    for input in inputs:
        delta = DIRECTION_MAP[input]
        position = position_map['santa' if is_santas_turn else 'robo-santa']
        position['x'] += delta['x']
        position['y'] += delta['y']
        key = f'{position["x"]},{position["y"]}'
        if key in houses:
            houses[key] += 1
        else:
            houses[key] = 1
        
        is_santas_turn = not is_santas_turn

    return len(houses.keys())


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
