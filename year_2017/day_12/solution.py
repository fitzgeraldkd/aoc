import os
from typing import Callable, List, Tuple

from utils.setup import read_inputs


def parse_input(input: str):
    program, connected_programs = input.strip().split(' <-> ')
    return int(program), [int(connected_program) for connected_program in connected_programs.split(', ')]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def build_network(pipes: List[Tuple[int, List[int]]]):
    network = {}

    for program, connected_programs in pipes:
        network[program] = connected_programs

    return network


def get_nodes_in_group(network, start):
    nodes_in_group = set()
    nodes_to_check = { start }

    while len(nodes_to_check) > 0:
        node_to_check = nodes_to_check.pop()
        nodes_in_group.add(node_to_check)
        for connected_program in network[node_to_check]:
            if connected_program not in nodes_in_group:
                nodes_to_check.add(connected_program)

    return nodes_in_group


def part_1(override_inputs = None):
    pipes = get_inputs(parse_input) if override_inputs is None else override_inputs
    network = build_network(pipes)

    return len(get_nodes_in_group(network, 0))


def part_2(override_inputs = None):
    pipes = get_inputs(parse_input) if override_inputs is None else override_inputs
    network = build_network(pipes)

    nodes_to_check = set(network.keys())
    groups = 0

    while len(nodes_to_check) > 0:
        node_to_check = nodes_to_check.pop()
        group = get_nodes_in_group(network, node_to_check)
        for node in group:
            nodes_to_check.discard(node)

        groups += 1

    return groups


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
