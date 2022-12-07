import math
import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.constants import ALPHABET
from utils.setup import read_inputs

PART_2_BASE_TIME = 60
PART_2_WORKERS = 5


def parse_input(input: str):
    _, prerequisite, _, _, _, _, _, dependent, _, _ = input.strip().split()
    return [prerequisite, dependent]


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    remaining = set()
    commands = defaultdict(set)
    order = []

    for prerequisite, dependent in instructions:
        commands[dependent].add(prerequisite)
        remaining.add(prerequisite) 
        remaining.add(dependent) 

    remaining = sorted(list(remaining))

    while len(remaining) > 0:
        for command in remaining:
            if len(commands[command]) == 0:
                order.append(command)
                remaining.remove(command)
                [commands[other].discard(command) for other in remaining]
                break

    return ''.join(order)


def part_2(override_inputs = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    remaining = set()
    commands = defaultdict(set)

    for prerequisite, dependent in instructions:
        commands[dependent].add(prerequisite)
        remaining.add(prerequisite) 
        remaining.add(dependent) 

    working = set()
    ready = []
    workers = []
    current_time = -1

    while remaining or working or ready:

        # Fast forward if all workers are busy.
        next_complete_time = min(workers, key=lambda worker: worker['time'])['time'] if workers else math.inf
        if len(workers) == PART_2_WORKERS and current_time < next_complete_time:
            current_time = next_complete_time
            continue

        # Clear the completed commands.
        for worker in workers:
            if worker['time'] <= current_time:
                working.remove(worker['command'])
                [commands[command].discard(worker['command']) for command in remaining]
                workers.remove(worker)

        for command in list(remaining):
            if len(commands[command]) == 0:
                remaining.remove(command)
                ready.append(command)
        ready = sorted(ready)

        # Assign workers.
        if ready and len(workers) < PART_2_WORKERS:
            available_workers = PART_2_WORKERS - len(workers)
            commands_to_start = ready[:available_workers]
            workers.extend([
                {'command': command, 'time': current_time + PART_2_BASE_TIME + ALPHABET.index(command.lower()) + 1} 
                for command in commands_to_start])
            ready = ready[available_workers:]
            [working.add(command) for command in commands_to_start]

        current_time += 1

    return current_time


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
