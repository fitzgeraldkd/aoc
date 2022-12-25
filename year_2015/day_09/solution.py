import math
import re

from classes.Graph import Graph
from utils.setup import read_inputs


def parse_input(input: str):
    split_input = re.split(r' to | = ', input.strip())
    return {
        'start': split_input[0],
        'end': split_input[1],
        'distance': int(split_input[2])
    }


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def get_distances(graph, start: str, previous_key: tuple, distances, remaining_nodes: set):
    previous_distance = distances[previous_key] if previous_key in distances else 0

    for node in graph.nodes[start].adjacent.keys():
        if node not in remaining_nodes:
            continue

        key = (*previous_key, node)

        distances[key] = previous_distance + graph.nodes[start].adjacent[node]

        sub_remaining_nodes = remaining_nodes.copy()
        sub_remaining_nodes.remove(node)
        get_distances(graph, start=node, previous_key=key, distances=distances, remaining_nodes=sub_remaining_nodes)

    return distances


def part_1():
    inputs = get_inputs()
    graph = Graph()
    locations = set()

    for input in inputs:
        locations.add(input['start'])
        locations.add(input['end'])
        graph.add_node(input['start'])
        graph.add_node(input['end'])
        graph.connect_nodes(input['start'], input['end'], input['distance'])

    distances = {}
    for node in graph.nodes.keys():
        distances = get_distances(graph, start=node, previous_key=(node, ), distances=distances,
                                  remaining_nodes=set(filter(lambda n: n != node, graph.nodes.keys())))

    min_distance = math.inf
    for key in distances.keys():
        if len(key) == len(locations) and distances[key] < min_distance:
            min_distance = distances[key]

    return min_distance


def part_2():
    inputs = get_inputs()
    graph = Graph()
    locations = set()

    for input in inputs:
        locations.add(input['start'])
        locations.add(input['end'])
        graph.add_node(input['start'])
        graph.add_node(input['end'])
        graph.connect_nodes(input['start'], input['end'], input['distance'])

    distances = {}
    for node in graph.nodes.keys():
        distances = get_distances(graph, start=node, previous_key=(node, ), distances=distances,
                                  remaining_nodes=set(filter(lambda n: n != node, graph.nodes.keys())))

    max_distance = 0
    for key in distances.keys():
        if len(key) == len(locations) and distances[key] > max_distance:
            max_distance = distances[key]

    return max_distance


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
