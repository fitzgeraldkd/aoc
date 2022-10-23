import itertools
import operator
import os
import re
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import DIRECTIONS


def parse_input(input: str):
    input = input.strip()
    if input.startswith('/'):
        split_input = re.split(r'\s+', input)
        path = split_input[0].split('-')
        node = (int(path[1][1:]), int(path[2][1:]))
        data = {
            'size': int(split_input[1][:-1]),
            'used': int(split_input[2][:-1]),
            'avail': int(split_input[3][:-1]),
            'use%': int(split_input[4][:-1])
        }
        return node, data
    else:
        return None


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    nodes = {}
    file = open(f'{script_dir}/inputs.txt')
    for line in file.readlines():
        parsed_line = parse_input(line)
        if parsed_line is not None:
            nodes[parsed_line[0]] = parsed_line[1]
    file.close()
    return nodes


def is_viable(node_a: dict, node_b: dict):
    if node_a['used'] == 0:
        return False
    if node_b['avail'] < node_a['used']:
        return False
    
    return True


def part_1():
    nodes = get_inputs()
    permutations = list(itertools.permutations(nodes.keys(), 2))

    viable_count = 0
    for position_a, position_b in permutations:
        if is_viable(nodes[position_a], nodes[position_b]):
            viable_count += 1

    return viable_count


def get_adjacent(position: tuple):
    return [tuple(map(operator.add, position, direction)) for direction in DIRECTIONS]


def part_2():
    nodes = get_inputs()
    max_x = 0

    # Nodes too full that will never be able to move data to an adjacent node (even if the adjacent node is emptied).
    too_full = []
    for position in nodes:
        max_x = max(max_x, position[0])
        for adjacent in get_adjacent(position):
            if adjacent not in nodes:
                continue
            if nodes[position]['used'] < nodes[adjacent]['size']:
                continue
                too_full.append(position)


    goal = (max_x, 0)
    absolute_max = nodes[(0, 0)]['size']

    print(too_full)
    print(max_x)
    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
