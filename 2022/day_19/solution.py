import os
import sys
from functools import reduce
from tqdm import tqdm
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import get_tqdm_kwargs, read_inputs


ROBOTS = ['ore', 'clay', 'obsidian', 'geode']

def get_blueprint(id, ore_ore, clay_ore, obsidian_ore, obsidian_clay, geode_ore, geode_obsidian):
    return {
        'id': id,
        'ore': {
            'ore': ore_ore
        },
        'clay': {
            'ore': clay_ore
        },
        'obsidian': {
            'ore': obsidian_ore,
            'clay': obsidian_clay
        },
        'geode': {
            'ore': geode_ore,
            'obsidian': geode_obsidian
        }
    }


def parse_input(input: str):
    _, id, _, _, _, _, ore_ore, _, _, _, _, _, clay_ore, _, _, _, _, _, obsidian_ore, _, _, obsidian_clay, _, _, _, _, _, geode_ore, _, _, geode_obsidian, *_ = input.strip().split(' ')
    return get_blueprint(int(id[:-1]), int(ore_ore), int(clay_ore), int(obsidian_ore), int(obsidian_clay),
                         int(geode_ore), int(geode_obsidian))


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    # return [parser(line) for line in read_inputs(script_directory)]
    return [parser(line) for line in read_inputs(script_directory, 'sample.txt')]


def get_available_robots(blueprint, stash):
    available = []
    for robot in ROBOTS:
        if all(stash[resource] >= blueprint[robot][resource] for resource in blueprint[robot]):
            available.append(robot)
    return available


def get_optimal_geodes(blueprint, robots, stash, duration, skipped, t=0):

    new_stash = {resource: stash[resource] + robots[resource] for resource in ROBOTS}
    # print(t, robots, new_stash)

    # if (t > TARGET_TIME - blueprint['geode']['obsidian'] and robots['obsidian'] == 0) or \
    #         (t > TARGET_TIME - blueprint['obsidian']['clay'] - blueprint['geode']['obsidian'] and robots['clay'] == 0 and robots['obsidian'] == 0):
    #     return 0

    if t < duration:
        available_robots = get_available_robots(blueprint, stash)
        # if 'geode' not in available_robots:
        if len(available_robots) != len(ROBOTS):
            possible_geodes = get_optimal_geodes(blueprint, robots, new_stash, duration, { *skipped, *available_robots }, t + 1)
        else:
            possible_geodes = stash['geode']

        if blueprint['geode']['ore'] <= robots['ore'] and blueprint['geode']['obsidian'] <= robots['obsidian']:
            remaining = duration - t
            return stash['geode'] + remaining * robots['geode'] + remaining * ((remaining + 1) // 2)

        for new_robot in [robot for robot in available_robots if robot not in skipped]:
            if new_robot == 'ore' and (t + 1 >= duration or robots['ore'] >= max(blueprint[robot].get('ore', 0) for robot in ROBOTS)):
                continue
            if new_robot == 'clay' and (t + 3 >= duration or robots['clay'] >= blueprint['obsidian']['clay']):
                continue
            if new_robot == 'obsidian' and (t + 2 >= duration or robots['obsidian'] >= blueprint['geode']['obsidian']):
                continue
            # if (new_robot == 'clay' and t + 3 >= TARGET_TIME) or (new_robot == 'obsidian' and t + 2 >= TARGET_TIME) or (new_robot == 'ore' and t + 1 >= TARGET_TIME):
            #     continue
            possible_geodes = max(possible_geodes, get_optimal_geodes(
                blueprint,
                {robot: robots[robot] + (1 if new_robot == robot else 0) for robot in ROBOTS},
                {resource: new_stash[resource] - blueprint[new_robot].get(resource, 0) for resource in ROBOTS},
                duration,
                skipped=set(),
                t=t + 1
            ))
        return possible_geodes
    else:
        return stash['geode']


def part_1(override_inputs = None):
    blueprints = get_inputs(parse_input) if override_inputs is None else override_inputs
    total_quality_level = 0

    for blueprint in tqdm(blueprints):
        geodes = get_optimal_geodes(
            blueprint,
            robots={'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0},
            stash={'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0},
            duration=24,
            skipped=set()
        )
        print(blueprint, geodes)
        total_quality_level += blueprint['id'] * geodes

    return total_quality_level


def part_2(override_inputs = None):
    blueprints = get_inputs(parse_input) if override_inputs is None else override_inputs

    geodes = []

    for blueprint in tqdm(blueprints[:3]):
        print(geodes)
        geodes.append(get_optimal_geodes(
            blueprint,
            robots={'ore': 1, 'clay': 0, 'obsidian': 0, 'geode': 0},
            stash={'ore': 0, 'clay': 0, 'obsidian': 0, 'geode': 0},
            duration=32,
            skipped=set()
        ))

    print(geodes)
    return reduce(lambda a, b: a * b, geodes)


if __name__ == '__main__':
    print('Part 1:', part_1())
    # print('Part 2:', part_2())
