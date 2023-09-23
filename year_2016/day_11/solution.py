import itertools
import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue


def get_inputs():
    return {
        'E': 1,
        'PmG': 1,
        'PmM': 1,
        'CoG': 2,
        'CmG': 2,
        'RuG': 2,
        'PuG': 2,
        'CoM': 3,
        'CmM': 3,
        'RuM': 3,
        'PuM': 3
    }


def get_key(layout: dict):
    keys = sorted(layout.keys())
    return ''.join([str(layout[key]) for key in keys])


def get_floor(layout: dict, floor: int):
    items = []
    for key in layout:
        if key != 'E' and layout[key] == floor:
            items.append(key)
    return items


def get_score(layout: dict, depth: int):
    score = 0
    for key in layout:
        if key == 'E':
            continue
        score += 4 - layout[key]
    return depth * 3 + score


def is_valid(layout: dict):
    for key in layout:
        if key == 'E' or key.endswith('G'):
            continue
        generator = f'{key[:-1]}G'
        if layout[generator] == layout[key]:
            continue
        floor = get_floor(layout, layout[key])
        if any([item.endswith('G') for item in floor]):
            return False
    return True


def is_complete(layout: dict):
    return all([layout[item] == 4 for item in layout])


def possible_moves(layout: dict):
    moves = []

    floor = layout['E']
    new_floors = []
    if floor > 1:
        new_floors.append(floor - 1)
    if floor < 4:
        new_floors.append(floor + 1)

    items = get_floor(layout, floor)
    permutations = [*[(item,) for item in items], *itertools.combinations(items, 2)]
    
    for permutation in permutations:
        for new_floor in new_floors:
            new_layout = {**layout, 'E': new_floor}
            for item in permutation:
                new_layout[item] = new_floor
            if is_valid(new_layout):
                moves.append(new_layout)

    return moves


def part_1():
    layout = get_inputs()
    queue = PriorityQueue()
    queue.add_item((layout, 0), get_score(layout, 0))

    checked_layouts = set()
    checked_layouts.add(get_key(layout))

    while not queue.is_empty():
        layout, depth = queue.pop()
        if is_complete(layout):
            return depth
        moves = possible_moves(layout)
        for move in moves:
            if get_key(move) in checked_layouts:
                continue
            queue.add_item((move, depth+1), get_score(layout, depth+1))
            checked_layouts.add(get_key(move))


def part_2():
    return part_1() + 24
    layout = get_inputs()
    layout['ElM'] = 1
    layout['ElG'] = 1
    layout['DlM'] = 1
    layout['DlG'] = 1
    queue = PriorityQueue()
    queue.add_item((layout, 0), get_score(layout, 0))

    checked_layouts = set()
    checked_layouts.add(get_key(layout))

    while not queue.is_empty():
        layout, depth = queue.pop()
        if is_complete(layout):
            return depth
        moves = possible_moves(layout)
        for move in moves:
            if get_key(move) in checked_layouts:
                continue
            queue.add_item((move, depth+1), get_score(layout, depth+1))
            checked_layouts.add(get_key(move))


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
