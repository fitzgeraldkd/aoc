import math
import os
import re

from classes.Graph import Graph


def parse_input(input: str):
    split_input = re.split(r' to | = ', input.strip())
    return {
        'start': split_input[0],
        'end': split_input[1],
        'distance': int(split_input[2])
    }


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def get_distances(graph, start: str, previous_key: str = '', distances = {}, remaining_nodes: set = set()):
    previous_distance = distances[previous_key] if previous_key in distances else 0

    for node in graph.nodes[start].adjacent.keys():
        if node not in remaining_nodes:
            continue

        key = f'{previous_key}{" -> " if previous_key else ""}{node}'

        distances[key] = previous_distance + graph.nodes[start].adjacent[node]

        sub_remaining_nodes = remaining_nodes.copy()
        sub_remaining_nodes.remove(node)
        get_distances(graph, node, key, distances, sub_remaining_nodes)

    return distances


def part_1():
    inputs = get_inputs()
    graph = Graph()

    for input in inputs:
        graph.add_node(input['start'])
        graph.add_node(input['end'])
        graph.connect_nodes(input['start'], input['end'], input['distance'])

    distances = {}
    for node in graph.nodes.keys():
        distances = get_distances(graph, node, node, distances, remaining_nodes=set(filter(lambda n: n != node, graph.nodes.keys())))

    min_distance = math.inf
    for key in distances.keys():
        if len(key) == 89 and distances[key] < min_distance:
            min_distance = distances[key]

    return min_distance


def part_2():
    inputs = get_inputs()
    graph = Graph()

    for input in inputs:
        graph.add_node(input['start'])
        graph.add_node(input['end'])
        graph.connect_nodes(input['start'], input['end'], input['distance'])

    distances = {}
    for node in graph.nodes.keys():
        distances = get_distances(graph, node, node, distances, remaining_nodes=set(filter(lambda n: n != node, graph.nodes.keys())))

    max_distance = 0
    for key in distances.keys():
        if len(key) == 89 and distances[key] > max_distance:
            max_distance = distances[key]

    return max_distance


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
