import hashlib
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue

OPEN_DOOR = ['b', 'c', 'd', 'e', 'f']
DIRECTIONS = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0)
}


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def get_hash(path: str):
    passcode = get_inputs()
    return hashlib.md5(f'{passcode}{path}'.encode('utf-8')).hexdigest()


def get_neighbors(path: str, location):
    neighbors = []
    hash = get_hash(path)
    if hash[0] in OPEN_DOOR and location[1] > 0:
        neighbors.append((f'{path}U', (location[0], location[1] - 1)))
    if hash[1] in OPEN_DOOR and location[1] < 3:
        neighbors.append((f'{path}D', (location[0], location[1] + 1)))
    if hash[2] in OPEN_DOOR and location[0] > 0:
        neighbors.append((f'{path}L', (location[0] - 1, location[1])))
    if hash[3] in OPEN_DOOR and location[0] < 3:
        neighbors.append((f'{path}R', (location[0] + 1, location[1])))
    return neighbors


def get_distance(location: tuple):
    return 6 - location[0] - location[1]


def part_1():
    queue = PriorityQueue()
    queue.add_item(('', (0, 0)), 6)
    while not queue.is_empty():
        path, location = queue.pop()
        if location == (3, 3):
            return path
        neighbors = get_neighbors(path, location)
        for neighbor in neighbors:
            queue.add_item(neighbor, len(neighbor[0]) + get_distance(neighbor[1]))


def part_2():
    queue = PriorityQueue()
    queue.add_item(('', (0, 0)), 6)
    longest = 0
    while not queue.is_empty():
        path, location = queue.pop()
        if location == (3, 3):
            longest = max(longest, len(path))
            continue
        neighbors = get_neighbors(path, location)
        for neighbor in neighbors:
            queue.add_item(neighbor, -1 * (len(neighbor[0]) + get_distance(neighbor[1])))
    return longest


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
