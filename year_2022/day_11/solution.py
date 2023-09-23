import numpy as np
import os
import sys
from typing import Callable, List

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.lists import split
from utils.setup import read_inputs


def parse_input(input: List[str]):
    _, items, operation, test, recipient_if_true, recipient_if_false = [line.strip() for line in input]
    return {
        'items': [int(item) for item in items.split(': ')[-1].split(', ')],
        'operation': lambda old: eval(operation.split('= ')[-1]),
        'test_value': int(test.split()[-1]),
        'inspections': 0,
        'recipients': {
            True: int(recipient_if_true.split()[-1]),
            False: int(recipient_if_false.split()[-1])
        }
    }


def get_inputs(parser: Callable):
    inputs = read_inputs(__file__)
    grouped_inputs = split(inputs, '\n')
    return [parser(group) for group in grouped_inputs]


def part_1(override_inputs = None):
    monkeys = get_inputs(parse_input) if override_inputs is None else override_inputs

    for _ in range(20):
        for monkey in monkeys:
            monkey['items'] = [monkey['operation'](item) // 3 for item in monkey['items']]
            monkey['inspections'] += len(monkey['items'])
            monkeys[monkey['recipients'][True]]['items'].extend(
                list(filter(lambda item: item % monkey['test_value'] == 0, monkey['items'])))
            monkeys[monkey['recipients'][False]]['items'].extend(
                list(filter(lambda item: item % monkey['test_value'] != 0, monkey['items'])))
            monkey['items'] = []

    inspections = sorted([monkey['inspections'] for monkey in monkeys])
    return inspections[-2] * inspections[-1]


def part_2(override_inputs = None):
    monkeys = get_inputs(parse_input) if override_inputs is None else override_inputs

    test_lcm = np.lcm.reduce([monkey['test_value'] for monkey in monkeys])

    for _ in range(10000):
        for monkey in monkeys:
            monkey['items'] = [monkey['operation'](item) % test_lcm for item in monkey['items']]
            monkey['inspections'] += len(monkey['items'])
            monkeys[monkey['recipients'][True]]['items'].extend(
                list(filter(lambda item: item % monkey['test_value'] == 0, monkey['items'])))
            monkeys[monkey['recipients'][False]]['items'].extend(
                list(filter(lambda item: item % monkey['test_value'] != 0, monkey['items'])))
            monkey['items'] = []

    inspections = sorted([monkey['inspections'] for monkey in monkeys])
    return inspections[-2] * inspections[-1]


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
