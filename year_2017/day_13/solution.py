from typing import Callable, List, Tuple

from utils.setup import read_inputs


def parse_input(input: str):
    return tuple(int(value) for value in input.strip().split(': '))


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def get_scanner_position(fw_range: int, time: int):
    cycle_duration = fw_range * 2 - 2
    time_in_cycle = time % cycle_duration
    return time_in_cycle if time_in_cycle < fw_range else cycle_duration - time_in_cycle


def part_1(override_inputs: List[Tuple[int, int]] = None):
    layers = get_inputs(parse_input) if override_inputs is None else override_inputs

    severity = 0

    for layer in layers:
        depth, fw_range = layer
        if get_scanner_position(fw_range, depth) == 0:
            severity += depth * fw_range

    return severity


def check_if_caught(layers: List[Tuple[int, int]], delay: int):
    for layer in layers:
        depth, fw_range = layer
        if get_scanner_position(fw_range, depth + delay) == 0:
            return True
    return False


def part_2(override_inputs: List[Tuple[int, int]] = None):
    layers = get_inputs(parse_input) if override_inputs is None else override_inputs

    start = 0
    step = 1

    for layer in layers:
        _, fw_range = layer
        if fw_range == 2:
            odds_only = check_if_caught([layer], 0)
            start = 1 if odds_only else 0
            step = 2


    for delay in range(start, 10000000, step):
        if not check_if_caught(layers, delay):
            break

    return delay


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
