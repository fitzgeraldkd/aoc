import operator
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import a_star, DIRECTIONS

def parse_input(input: str):
    return int(input.strip())


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def get_is_wall(location: tuple):
    x, y = location
    if min(x, y) < 0:
        return True
    foo = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + get_inputs()
    binary = '{0:b}'.format(foo)
    return binary.count('1') % 2 == 1


def get_heuristic(location: tuple, goal: tuple):
    return abs(location[0] - goal[0]) + abs(location[1] - goal[1])


def print_map(size: int):
    for y in range(size):
        row = []
        for x in range(size):
            is_wall = get_is_wall((x, y))
            row.append('#' if is_wall else '.')
        print(''.join(row))

def part_1():
    path = a_star((1, 1), (31, 39), get_is_wall, get_heuristic)
    return len(path) - 1


def part_2():
    locations = { (1, 1) }
    nodes = { (1, 1) }
    for _ in range(50):
        neighbors = set()
        for current in nodes:
            for neighbor in [tuple(map(operator.add, current, direction)) for direction in DIRECTIONS]:
                if not get_is_wall(neighbor):
                    locations.add(neighbor)
                    neighbors.add(neighbor)
        nodes = neighbors
    
    return len(locations)



if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
