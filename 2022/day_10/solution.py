import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    cmd = input.strip().split()
    if len(cmd) > 1:
        cmd[-1] = int(cmd[-1])
    else:
        cmd.append(None)
    return cmd


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def part_1(override_inputs = None):
    commands = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = 0

    targets = [220, 180, 140, 100, 60, 20]

    cycle = 1
    x = 1
    prev_x = 1
    for cmd, amount in commands:

        if cycle >= targets[-1]:
            this_x = prev_x if cycle > targets[-1] else x
            output += this_x * targets.pop()
            if not targets:
                break
        if cmd == 'noop':
            cycle += 1
        else:
            prev_x = x
            x += amount
            cycle += 2

    return output


def part_2(override_inputs = None):
    commands = get_inputs(parse_input) if override_inputs is None else override_inputs

    screen = [['.' for _ in range(40)] for _ in range(6)]

    command_index = -1
    current_command = [['noop', None], 0]
    x = 1

    for cycle in range(240):
        row = cycle // 40
        column = cycle % 40

        if current_command[1] == 0:
            command_index += 1
            if current_command[0][0] == 'addx':
                x += current_command[0][1]
            current_command = [commands[command_index], 1 if commands[command_index][0] == 'noop' else 2]

        current_command[1] -= 1

        if abs(x - column) <= 1:
            screen[row][column] = '#'

    for row in screen:
        print(''.join(row))

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
