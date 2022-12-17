import math
import os
import sys
from itertools import permutations
from tqdm import tqdm, trange
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.Graph import Graph
from classes.PriorityQueue import PriorityQueue
from utils.setup import get_tqdm_kwargs, read_inputs


def parse_input(input: str):
    _, valve, _, _, flow, _, _, _, _, *adjacent = input.split()
    # print(tunnels)
    return {
        'label': valve,
        'flow': int(flow[:-1].split('=')[-1]),
        'adjacent': ''.join(adjacent).split(',')
    }
    return input.strip()
    return int(input.strip())


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    # return {valve['label']: {**valve} for valve in [parser(line) for line in read_inputs(script_directory)]}
    return [parser(line) for line in read_inputs(script_directory)]
    return [parser(line) for line in read_inputs(script_directory, 'sample.txt')]


def get_available_actions(valves: dict, location: str, open_valves: set):
    actions = []

    if len(open_valves) == len(valves.keys()):
        return actions

    actions.extend([('move', valve) for valve in valves[location]['adjacent'].keys() if valve != location and valve not in open_valves])

    if valves[location]['flow'] > 0 and location not in open_valves:
        actions.append(('open', location))

    return actions


def take_actions(valves: dict, location: str, open_valves: set, time: int, relieved: int, action: tuple):
    # checked_state
    # print(location, open_valves, time, relieved, action)
    if action[0] == 'move':
        # print(valves[location]['adjacent'])
        delta_time = valves[location]['adjacent'][action[1]]
        location = action[1]
    elif action[0] == 'open':
        # print('hi')
        delta_time = 1
        open_valves.add(action[1])
    elif action[0] == 'wait':
        delta_time = math.inf
    # print(delta_time)
    # TODO: Check if off by one.
    delta_time = min(delta_time, 30 - time)
    relieved += delta_time * sum([valves[valve]['flow'] for valve in open_valves])
    return location, open_valves, time + delta_time, relieved


def get_distance(valves, valve_a, valve_b):
    print(valve_a, valve_b)
    input()
    if valve_b in valves[valve_a]['adjacent']:
        return 1
    else:
        return 1 + min(get_distance(valves, valve_between, valve_b) for valve_between in valves[valve_a]['adjacent'])


def get_valves_with_flow(valves):
    valves_with_flow = [{**valve} for valve in valves.values() if valve['flow'] > 0]
    for valve in valves_with_flow:
        new_adjacent = []
        for other_valve in valves_with_flow:
            if other_valve == valve:
                continue
            # print(other_valve)
            distance = get_distance(valves, valve['label'], other_valve['label'])
        # print(valve)
        # valve['adjacent'] = [(valve_with_flow['label'], get_distance(valves, valve['label'], valve_with_flow['label']))
        #                      for valve_with_flow in valves_with_flow if valve_with_flow['label'] != valve['label']]
        # for adjacent in valve['adjacent']:
    return valves_with_flow




def part_1(override_inputs = None):
    valves = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = None

    # valves_with_flow = get_valves_with_flow(valves)
    # print(valves_with_flow)
    # input()

    network = Graph()
    for valve in valves:
        network.add_node(valve['label'])
        for adjacent in valve['adjacent']:
            if adjacent in network.nodes:
                network.connect_nodes(valve['label'], adjacent, 1)

    # print(network.nodes)
    # print(network.nodes['AA'].adjacent)
    # print(network.shortest_distance('AA', 'CC'))
    # print(network.dijkstra('AA'))
    distances = {valve['label']: network.dijkstra(valve['label']) for valve in valves}
    # print(distances['AA'])
    # print(distances)

    valves_with_flow = {}
    for valve in valves:
        if valve['flow'] == 0 and valve['label'] != 'AA':
            for distance in distances.values():
                del distance[valve['label']]
        else:
            valves_with_flow[valve['label']] = {
                **valve,
                'adjacent': distances[valve['label']]
            }

    # valves_with_flow['AA'] = {
    #     **valves['AA'],
    #     'adjacent': distances['AA']
    # }

    # print(distances)
    # print(valves_with_flow)

    # location = 'AA'
    # open_valves = set()
    # actions = get_available_actions(valves_with_flow, location, open_valves)
    # stack = [{
    #     'action': action,
    #     'time': 0,
    #     'location': location,
    #     'open_valves': open_valves,
    #     'relieved': 0
    # } for action in actions]

    # max_relieved = 0
    # print(actions)

    # while stack:
    #     state = stack.pop()
    #     # print(state)
    #     # print(state)
    #     # input()
    #     location, open_valves, time, relieved = take_actions(valves_with_flow, state['location'], state['open_valves'], state['time'], state['relieved'], state['action'])
    #     if time >= 30:
    #         max_relieved = max(max_relieved, relieved)
    #         print(max_relieved, len(stack))
    #     else:
    #         new_actions = get_available_actions(valves_with_flow, location, set(open_valves))
    #         # print(new_actions)
    #         stack.extend([{
    #             'action': new_action,
    #             'time': time,
    #             'location': location,
    #             'open_valves': set(open_valves),
    #             'relieved': relieved
    #         } for new_action in new_actions])

    # return max_relieved

    # print(valves_with_flow)
    # for valve in valves_with_flow.values():
    #     print(valve)

    highest_relieved = 0

    def calc_relieved(path):
        time = 0
        relieved = 0
        for i in range(len(path) - 1):
            current_valve = path[i]
            next_valve = path[i + 1]
            distance = valves_with_flow[current_valve]['adjacent'][next_valve]
            time += distance + 1
            relieved += sum(valves_with_flow[valve]['flow'] for valve in path[:i+1]) * (distance)
            relieved += sum(valves_with_flow[valve]['flow'] for valve in path[:i+2])
            # relieved += valves_with_flow[next_valve]['flow']

        relieved += (29 - time) * sum(valves_with_flow[valve]['flow'] for valve in path)

        if relieved == 223375:
            print('THE PATH')
            print(path)

        # print(path, relieved, time, sum(valves_with_flow[valve]['flow'] for valve in path))

        return relieved

    def get_relieved(current_path):
        time = 0
        new_paths = []
        max_relieved = 0
        for i in range(len(current_path) - 1):
            time += valves_with_flow[current_path[i]]['adjacent'][current_path[i + 1]] + 1
        # print(time)


        for valve in valves_with_flow:
            distance = valves_with_flow[current_path[-1]]['adjacent'][valve]
            if valve not in current_path and time + distance < 30:
                new_paths = get_paths([*current_path, valve])
                # print(new_paths)
                max_relieved = max(max_relieved, *[calc_relieved(path) for path in new_paths])
                # new_paths.extend(get_paths([*current_path, valve]))

        if len(new_paths) == 0:
            # highest_relieved = max(highest_relieved, get_relieved(current_path))
            # highest_relieved += 1
            return [current_path]

        return max_relieved


    def get_paths(current_path):
        time = 0
        new_paths = []
        for i in range(len(current_path) - 1):
            time += valves_with_flow[current_path[i]]['adjacent'][current_path[i + 1]] + 1
        # print(time)


        for valve in valves_with_flow:
            distance = valves_with_flow[current_path[-1]]['adjacent'][valve]
            if valve not in current_path and time + distance < 30:
                new_paths.extend(get_paths([*current_path, valve]))

        if len(new_paths) == 0:
            # highest_relieved = max(highest_relieved, get_relieved(current_path))
            # highest_relieved += 1
            return [current_path]

        return new_paths


    paths = get_paths(['AA'])
    print(get_relieved(['AA']))

    # print(valves_with_flow)
    return get_relieved(['AA'])

    paths = permutations(valves_with_flow.keys())

    valves_with_flow['AA'] = {
        **valves['AA'],
        'adjacent': distances['AA']
    }
    # print(list(paths))
    # print(len(list(paths)))

    max_relieved = 0

    # for path in tqdm(paths, **get_tqdm_kwargs(__file__, 1)):
    for path in paths:
        relieved = 0
        location = 'AA'
        time = 0
        open_valves = set()
        for step in path:
            # Move.
            delta_time = valves_with_flow[location]['adjacent'][step]
            location = step

            delta_time = min(delta_time, 30 - time - 1)
            relieved += delta_time * sum([valves_with_flow[valve]['flow'] for valve in open_valves])
            time += delta_time
            if time >= 30:
                break

            # Open.
            delta_time = 1
            open_valves.add(step)
            relieved += sum([valves_with_flow[valve]['flow'] for valve in open_valves])
            time += 1
            if time >= 30:
                break

        delta_time = 30 - time - 1
        relieved += delta_time * sum([valves_with_flow[valve]['flow'] for valve in open_valves])
        max_relieved = max(max_relieved, relieved)
        print(max_relieved)

    return max_relieved



    # print(inputs)

    # state = {
    #     'open_valves': set(),
    #     'location': 'AA',
    #     'time': 0,
    #     'relieved': 0
    # }

    # queue = PriorityQueue()
    # queue.add_item(state, state['relieved'])
    # # queue.add_item('foo', 50)
    # # print('TESTING', queue.pop())

    # checked_states = set()

    # max_relieved = 0

    # while len(queue) > 0:
    #     state = queue.pop()
    #     checked_states.add((state['location'], tuple(state['open_valves'])))
    #     # print(state['time'], len(queue), max_relieved, state['location'], state['open_valves'])
    #     # print(state['location'])
    #     # print(valves[state['location']])
    #     # print(valves[state['location']]['adjacent'])
    #     available_moves = []
    #     available_moves = [('move', valves[valve]['label']) for valve in valves[state['location']]['adjacent']]
    #     if state['location'] not in state['open_valves'] and valves[state['location']]['flow'] > 0:
    #         available_moves.append(('open', state['location']))

    #     for action, valve in available_moves:
    #         new_location = state['location']
    #         new_open_valves = set(state['open_valves'])
    #         new_time = state['time'] + 1

    #         if action == 'move':
    #             new_location = valve
    #         elif action == 'open':
    #             new_open_valves.add(valve)

    #         # TODO: Check if off-by-one.
    #         new_relieved = state['relieved'] + sum([valve['flow'] for valve in valves.values() if valve['label'] in new_open_valves])

    #         if new_time == 30:
    #             max_relieved = max(max_relieved, new_relieved)
    #             print(max_relieved)
    #             continue

    #         new_state = {
    #             'open_valves': new_open_valves,
    #             'location': new_location,
    #             'time': new_time,
    #             'relieved': new_relieved
    #         }

    #         if len(new_open_valves) == len(valves.keys()):
    #             print('ALL VALVES OPEN')
    #             break

    #         # if (new_state['location'], tuple(new_state['open_valves'])) not in checked_states:
    #         queue.add_item(new_state, -1 * new_state['relieved'])

    # return output


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = None

    for input in tqdm(inputs):
        pass

    return output


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
