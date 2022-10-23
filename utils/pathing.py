import math
import operator
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue


DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def a_star(start: tuple, goal: tuple, get_is_wall, get_heuristic):
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
        
        for neighbor in [tuple(map(operator.add, current, direction)) for direction in DIRECTIONS]:
            if get_is_wall(neighbor):
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
