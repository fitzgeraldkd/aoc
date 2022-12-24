import math
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue
from utils.setup import read_inputs

AMPHIPODS = 'ABCD'

def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    board = {}
    for coord in [(0, 0), (1, 0), (2, 1), (2, 2), (3, 0), (4, 1), (4, 2), (5, 0), (6, 1), (6, 2), (7, 0), (8, 1),
                  (8, 2), (9, 0), (10, 0)]:
        board[coord] = None
    for y, line in enumerate(read_inputs(__file__)[2:4], start=1):
        for x, amphipod in enumerate(line[3:10:2]):
            board[(2 + 2 * x, y)] = amphipod
    return {
        'board': board,
        'energy': 0
    }


def get_available_positions(state: dict, location: tuple):
    available_positions = []

    board = state['board']
    amphipod = board[location]

    if amphipod is None or (location[1] == 2 and board[(location[0], 1)] is not None):
        return []

    if location[0] == (AMPHIPODS.index(amphipod) + 1) * 2:
        if location[1] == 2:
            return []
        if location[1] == 1 and board[location[0], 2] == amphipod:
            return []

    for position, occupied in board.items():
        # Space already occupied.
        if occupied is not None:
            continue
        # Can't enter other amphipod rooms.
        if position[1] > 0 and position[0] != (AMPHIPODS.index(amphipod) + 1) * 2:
            continue
        # Can't move through amphipods.
        # if position[1] == 2 and board[(position[0], 1)] is not None:
        #     continue
        if any(board.get((x, 0)) is not None for x in range(min(location[0] + 1, position[0]), max(location[0], position[0]))):
            continue
        # Can't enter its own room if a different type of amphipod is in there.
        if position[1] == 1 and (board[(position[0], 2)] is None or board[(position[0], 2)] is not amphipod):
            continue
        # Can't wander hallway.
        if location[1] == 0 and position[1] == 0:
            continue

        available_positions.append(position)

    return available_positions




def get_distance(start: tuple, end: tuple):
    return abs(end[0] - start[0]) + start[1] + end[1]


def is_end_state(state: dict):
    for location, value in state['board'].items():
        if location[1] == 0 and value is not None:
            return False
        if value is not None and location[0] != (AMPHIPODS.index(value) + 1) * 2:
            return False
    return True


def is_in_end_position(state: dict, item: tuple):
    location, amphipod = item
    if location[1] == 0 or location[0] != (AMPHIPODS.index(amphipod) + 1) * 2:
        return False
    if location[1] == 1:
        return state['board'][(location[0], 2)] == amphipod
    return True


def get_min_energy_needed(state: dict):
    energy = 0

    for location, amphipod in state['board'].items():
        index = AMPHIPODS.index(amphipod) if amphipod is not None else -1
        x = (index + 1) * 2
        if amphipod is not None and not is_in_end_position(state, (location, amphipod)):
            energy += get_distance(location, (x, 1)) * (10 ** (index))

    return energy



def find_efficient_path(starting_state):
    get_key = lambda board: tuple(item for item in sorted(board.items(), key=lambda item: item[0]))

    states_to_check = PriorityQueue()
    states_to_check.add_item(starting_state, 0)
    # states_to_check = { get_key(starting_state['board']): starting_state['energy'] }
    checked_states = set()

    while states_to_check:
        # print(states_to_check.items[-1])
        state = states_to_check.pop()
        # print(state)
        if is_end_state(state):
            return state['energy']
        amphipods = [(start, amphipod) for start, amphipod in state['board'].items() if amphipod is not None]
        for start, amphipod in amphipods:
            available_positions = get_available_positions(state, start)
            for destination in available_positions:
                new_board = { **state['board'], start: None, destination: amphipod }
                new_energy = state['energy'] + get_distance(start, destination) * 10 ** (AMPHIPODS.index(amphipod))
                new_state = { 'board': new_board, 'energy': new_energy }
                if get_key(new_board) not in checked_states and not states_to_check.has_item(new_state):
                    states_to_check.add_item(new_state, new_energy + get_min_energy_needed(new_state))
        checked_states.add(get_key(state['board']))
    # if is_end_state(state):
    #     return state

    # min_energy = math.inf

    # amphipods = [(start, amphipod) for start, amphipod in state['board'].items() if amphipod is not None]
    # for start, amphipod in amphipods:
    #     available_positions = get_available_positions(state, start)
    #     for destination in sorted(available_positions, key=lambda position: get_distance(start, position) + get_distance(position, ((AMPHIPODS.index(amphipod) + 1) * 2, 2))):
    #         end_state = find_efficient_path({
    #             'board': {
    #                 **state['board'],
    #                 start: None,
    #                 destination: amphipod
    #             },
    #             'energy': state['energy'] + get_distance(start, destination) * 10 ** (AMPHIPODS.index(amphipod))
    #         })
    #         if end_state is not None:
    #             return end_state


def part_1(override_inputs = None):
    state = get_inputs(parse_input) if override_inputs is None else override_inputs
    # state = {
    #     'board': {
    #         (0, 0): None,
    #         (1, 0): None,
    #         (2, 1): 'D',
    #         (2, 2): 'C',
    #         (3, 0): None,
    #         (4, 1): 'A',
    #         (4, 2): 'C',
    #         (5, 0): None,
    #         (6, 1): 'A',
    #         (6, 2): 'B',
    #         (7, 0): None,
    #         (8, 1): 'D',
    #         (8, 2): 'B',
    #         (9, 0): None,
    #         (10, 0): None
    #     },
    #     'energy': 0
    # }

    # print(state)
    # print(get_available_positions(state, (2, 1)))
    # print(get_available_positions(state, (2, 2)))


    return find_efficient_path(state)


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
