import os
import sys

from collections import Counter
from typing import List

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def read_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    return file.readlines()


def parse_input(input: str):
    input = input.strip()
    program, parents = input.split(' -> ') if ' -> ' in input else (input, '')
    name, weight = program.split(' ')
    return {
        'name': name,
        'weight': int(weight[1:-1]),
        'parents': parents.split(', ') if parents else []
    }


def get_inputs():
    inputs = [parse_input(line) for line in read_inputs()]
    return inputs


def build_towers(programs: List[dict]):
    towers = {}
    for program in programs:
        towers[program['name']] = {
            'child': None,
            'name': program['name'],
            'parents': [],
            'total_weight': None,
            'weight': program['weight']
        }

    for program in programs:
        for parent in program['parents']:
            towers[program['name']]['parents'].append(towers[parent])
            towers[parent]['child'] = towers[program['name']]

    return towers


def part_1(override_inputs: List[dict] = None):
    programs = override_inputs or get_inputs()
    towers = build_towers(programs)

    program_name = programs[0]['name']
    while towers[program_name]['child'] is not None:
        program_name = towers[program_name]['child']['name']

    return program_name


def part_2(override_inputs: List[dict] = None):
    """
    Thoughts to improve:
    - Use a class for the towers and move all the methods into that class.
    - Starting from the bottom means that the weight for every tower needs to be calculated. It may be more efficient to
      start from the top.
    """
    programs = override_inputs or get_inputs()
    towers = build_towers(programs)

    def get_weight(towers, program_name):
        if towers[program_name]['total_weight'] is not None:
            return towers[program_name]['total_weight']

        weight = towers[program_name]['weight']
        for parent in towers[program_name]['parents']:
            weight += get_weight(towers, parent['name'])
        towers[program_name]['total_weight'] = weight
        return weight

    def get_unbalanced(towers, program_name):
        parent_weight = None
        parent_weights = []

        for parent in towers[program_name]['parents']:
            parent_weights.append({'name': parent['name'], 'weight': get_weight(towers, parent['name'])})

        weight_collection = Counter(parent['weight'] for parent in parent_weights)

        if len(weight_collection) > 1:
            (most_common_weight, _), (least_common_weight, _) = weight_collection.most_common(2)
            for parent in towers[program_name]['parents']:
                parent_weight = get_weight(towers, parent['name'])
                if parent_weight != most_common_weight:
                    return parent, least_common_weight - most_common_weight

        return None, 0

    program_name = part_1(override_inputs)
    weight_difference = 0
    while True:
        unbalanced_tower, difference = get_unbalanced(towers, program_name)
        if unbalanced_tower:
            program_name = unbalanced_tower['name']
            weight_difference = difference
        else:
            break

    return towers[program_name]['weight'] - weight_difference


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
