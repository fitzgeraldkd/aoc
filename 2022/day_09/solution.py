import operator
import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import DIRECTIONS
from utils.setup import read_inputs

DIRECTION_MAP = {
    'R': DIRECTIONS[0],
    'D': DIRECTIONS[1],
    'L': DIRECTIONS[2],
    'U': DIRECTIONS[3]
}


def parse_input(input: str):
    split_input = input.strip().split()
    return (split_input[0], int(split_input[1]))


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    head = (0, 0)
    tail = (0, 0)
    tail_visited = defaultdict(lambda: False)
    tail_visited[tail] = True

    for direction, distance in inputs:
        for _ in range(distance):
            new_head = tuple(map(operator.add, head, DIRECTION_MAP[direction]))
            delta_x = abs(new_head[0] - tail[0])
            delta_y = abs(new_head[1] - tail[1])
            if delta_x > 1 or delta_y > 1 or delta_x + delta_y > 2:
                tail = head
                tail_visited[tail] = True
            head = new_head

    return len(tail_visited.values())


def print_rope(rope):
    x_values = [segment[0] for segment in rope]
    y_values = [segment[1] for segment in rope]

    for y in range(min(y_values), max(y_values) + 1):
        row = []
        for x in range(min(x_values), max(x_values) + 1):
            row.append(str(rope.index((x, y))) if (x, y) in rope else '.')
        print(''.join(row))


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    rope = [(0, 0) for _ in range(10)]
    tail_visited = defaultdict(lambda: False)
    tail_visited[(0, 0)] = True

    for direction, distance in inputs:
        for _ in range(distance):
            new_rope = []
            for i in range(len(rope) - 1):
                head = rope[i]
                tail = rope[i + 1]
                if i == 0:
                    new_head = tuple(map(operator.add, head, DIRECTION_MAP[direction]))
                    new_rope.append(new_head)
                else:
                    new_head = new_rope[i]
                delta_x = abs(new_head[0] - tail[0])
                delta_y = abs(new_head[1] - tail[1])
                if (delta_x > 1 or delta_y > 1) and min(delta_x, delta_y) == 0:
                    step_x = int((new_head[0] - tail[0]) / delta_x) if delta_x else 0
                    step_y = int((new_head[1] - tail[1]) / delta_y) if delta_y else 0
                    new_position = tuple(map(operator.add, tail, (step_x, step_y)))
                    new_rope.append(new_position)
                    if i == len(rope) - 2:
                        tail_visited[new_position] = True
                elif delta_x + delta_y > 2:
                    step_x = int((new_head[0] - tail[0]) / delta_x)
                    step_y = int((new_head[1] - tail[1]) / delta_y)
                    new_position = tuple(map(operator.add, tail, (step_x, step_y)))
                    new_rope.append(new_position)
                    if i == len(rope) - 2:
                        tail_visited[new_position] = True
                else:
                    new_rope.extend(rope[i + 1:])
                    break
            rope = new_rope

    return len(tail_visited.values())


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
