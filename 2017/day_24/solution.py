import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return [int(value) for value in input.strip().split('/')]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    ports = get_inputs(parse_input) if override_inputs is None else override_inputs
    
    def build_bridge(bridge, pins, max_strength=0):
        available_ports = list(filter(lambda port: pins in port, [port for port in ports if port not in bridge]))
        if len(available_ports) == 0:
            return sum(sum(port) for port in bridge)
        else:
            for port in available_ports:
                strength = build_bridge([*bridge, port], port[1] if port[0] == pins else port[0])
                max_strength = max(strength, max_strength)
        
        return max_strength

    max_strength = build_bridge([], 0)

    return max_strength


def part_2(override_inputs = None):
    ports = get_inputs(parse_input) if override_inputs is None else override_inputs


    def build_bridge(bridge, pins, longest_bridges):
        available_ports = list(filter(lambda port: pins in port, [port for port in ports if port not in bridge]))
        if len(available_ports) == 0:
            if len(bridge) == len(longest_bridges[0]):
                longest_bridges = [*longest_bridges, bridge]
            elif len(bridge) > len(longest_bridges[0]):
                longest_bridges = [bridge]
            return longest_bridges
        else:
            for port in available_ports:
                longest_bridges = build_bridge([*bridge, port], port[1] if port[0] == pins else port[0], longest_bridges)
            return longest_bridges
    
    longest_bridges = build_bridge([], 0, [[]])

    return max(sum(sum(port) for port in bridge) for bridge in longest_bridges)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
