import math
import os
import sys
from tqdm import tqdm, trange
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.Graph import Graph
from utils.setup import get_tqdm_kwargs, read_inputs


def parse_input(input: str):
    _, valve, _, _, flow, _, _, _, _, *adjacent = input.split()
    return {
        'label': valve,
        'flow': int(flow[:-1].split('=')[-1]),
        'adjacent': ''.join(adjacent).split(',')
    }


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def get_valves_with_flow(valves):
    network = Graph()
    for valve in valves:
        network.add_node(valve['label'])
        for adjacent in valve['adjacent']:
            if adjacent in network.nodes:
                network.connect_nodes(valve['label'], adjacent, 1)

    distances = {valve['label']: network.dijkstra(valve['label']) for valve in valves}

    valves_with_flow = {}
    for valve in valves:
        if valve['flow'] == 0 and valve['label'] != 'AA':
            for distance in distances.values():
                del distance[valve['label']]
        else:
            valves_with_flow[valve['label']] = {
                **valve,
                'adjacent': distances[valve['label']]
            }

    return valves_with_flow


def calc_relieved(valves_with_flow, path, time=0):
    relieved = 0
    for i in range(len(path) - 1):
        delta_time = valves_with_flow[path[i]]['adjacent'][path[i + 1]] + 1
        time += delta_time
        relieved += sum(valves_with_flow[valve]['flow'] for valve in path[:i+1]) * delta_time

    relieved += (30 - time) * sum(valves_with_flow[valve]['flow'] for valve in path)

    return relieved


def get_max_relieved(valves_with_flow, current_path, time=0):
    for i in range(len(current_path) - 1):
        time += valves_with_flow[current_path[i]]['adjacent'][current_path[i + 1]] + 1

    is_in_range = lambda valve: time + valves_with_flow[current_path[-1]]['adjacent'][valve] < 30
    available_valves = list(filter(lambda valve: valve not in current_path and is_in_range(valve), valves_with_flow))

    if len(available_valves) == 0:
        return calc_relieved(valves_with_flow, current_path)
    else:
        return max([get_max_relieved(valves_with_flow, [*current_path, valve]) for valve in available_valves])


def part_1(override_inputs = None):
    valves = get_inputs(parse_input) if override_inputs is None else override_inputs
    valves_with_flow = get_valves_with_flow(valves)

    return get_max_relieved(valves_with_flow, ['AA'])


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = None

    for input in tqdm(inputs):
        pass

    return output


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
