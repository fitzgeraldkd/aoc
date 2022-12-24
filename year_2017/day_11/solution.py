from typing import Callable, Tuple

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip().split(',')


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)][0]


def move(position: Tuple[int, int], direction: str):
    x, y = position

    if direction == 'n':
        return (x, y + 2)
    elif direction == 'ne':
        return (x + 1, y + 1)
    elif direction == 'se':
        return (x + 1, y - 1)
    elif direction == 's':
        return (x, y - 2)
    elif direction == 'sw':
        return (x - 1, y - 1)
    elif direction == 'nw':
        return (x - 1, y + 1)


def get_distance(position: Tuple[int, int]):
    x, y = [abs(coordinate) for coordinate in position]
    due_east_west_distance = x - y if x > y else 0
    return ((x + y + due_east_west_distance) // 2)


def part_1(override_inputs = None):
    directions = get_inputs(parse_input) if override_inputs is None else override_inputs

    position = (0, 0)
    for direction in directions:
        position = move(position, direction)

    return get_distance(position)


def part_2(override_inputs = None):
    directions = get_inputs(parse_input) if override_inputs is None else override_inputs

    position = (0, 0)
    max_distance = 0
    for direction in directions:
        position = move(position, direction)
        max_distance = max(max_distance, get_distance(position))

    return max_distance


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
