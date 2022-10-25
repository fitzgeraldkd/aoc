import itertools
import math
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import a_star


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def get_locations(layout):
    locations = {}
    for y, row in enumerate(layout):
        for x, tile in enumerate(row):
            if tile not in '.#':
                locations[tile] = (x, y)
    return locations


def part_1():
    layout = get_inputs()
    locations = get_locations(layout)
    print(locations)
    pairings = list(itertools.combinations(locations, 2))
    print(pairings)

    def get_is_wall(coords: tuple):
        return layout[coords[1]][coords[0]] == '#'
    
    def get_heuristic(start: tuple, goal: tuple):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    distances = {}
    for pairing in pairings:
        distance = len(a_star(locations[pairing[0]], locations[pairing[1]], get_is_wall, get_heuristic)) - 1
        if pairing[0] in distances:
            distances[pairing[0]][pairing[1]] = distance
        else:
            distances[pairing[0]] = { pairing[1]: distance }
        if pairing[1] in distances:
            distances[pairing[1]][pairing[0]] = distance
        else:
            distances[pairing[1]] = { pairing[0]: distance }
    
    start = locations.pop('0')
    routes = list(itertools.permutations(locations))
    print(routes)

    min_route = ''
    min_distance = math.inf
    for route in routes:
        current = '0'
        distance = 0
        for node in route:
            distance += distances[current][node]
            current = node
        min_distance = min(distance, min_distance)
        min_route = route

    print(min_route)
    return min_distance


def part_2():
    layout = get_inputs()
    locations = get_locations(layout)
    print(locations)
    pairings = list(itertools.combinations(locations, 2))
    print(pairings)

    def get_is_wall(coords: tuple):
        return layout[coords[1]][coords[0]] == '#'
    
    def get_heuristic(start: tuple, goal: tuple):
        return abs(start[0] - goal[0]) + abs(start[1] - goal[1])

    distances = {}
    for pairing in pairings:
        distance = len(a_star(locations[pairing[0]], locations[pairing[1]], get_is_wall, get_heuristic)) - 1
        if pairing[0] in distances:
            distances[pairing[0]][pairing[1]] = distance
        else:
            distances[pairing[0]] = { pairing[1]: distance }
        if pairing[1] in distances:
            distances[pairing[1]][pairing[0]] = distance
        else:
            distances[pairing[1]] = { pairing[0]: distance }
    
    start = locations.pop('0')
    routes = list(itertools.permutations(locations))
    print(routes)

    min_route = ''
    min_distance = math.inf
    for route in routes:
        current = '0'
        distance = 0
        for node in route:
            distance += distances[current][node]
            current = node
        distance += distances[current]['0']
        min_distance = min(distance, min_distance)
        min_route = route

    print(min_route)
    return min_distance


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
