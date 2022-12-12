import math
import operator
import os
import sys
from typing import List, Tuple

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue


DIRECTIONS: List[Tuple[int, int]] = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


def get_adjacent(position: Tuple[int, int]):
    return [tuple(map(operator.add, position, direction)) for direction in DIRECTIONS]


def a_star(start: Tuple[int, int], goal: Tuple[int, int], get_is_wall, get_heuristic):
    queue = PriorityQueue()
    previous = {}
    g_score = { start: 0 }
    f_score = { start: get_heuristic(start, goal) }
    queue.add_item(start, f_score[start])

    while not queue.is_empty():
        current = queue.pop()

        if current == goal:
            path = []
            node = current
            while node != start:
                path.append(node)
                node = previous[node]
            path.append(start)
            return path

        for neighbor in get_adjacent(current):
            if get_is_wall(neighbor, current=current):
                continue
            neighbor_g_score = g_score[current] + 1
            if neighbor_g_score < g_score.get(neighbor, math.inf):
                previous[neighbor] = current
                g_score[neighbor] = neighbor_g_score
                f_score[neighbor] = neighbor_g_score + get_heuristic(neighbor, goal)
                if queue.has_item(neighbor):
                    queue.update_priority(neighbor, f_score[neighbor])
                else:
                    queue.add_item(neighbor, f_score[neighbor])
