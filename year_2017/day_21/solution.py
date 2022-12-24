from typing import Callable, List

from utils.setup import read_inputs


STARTING_BOARD = [
    '.#.',
    '..#',
    '###'
]


class Board:
    def __init__(self, rule_map):
        self.rule_map = rule_map
        self.state = STARTING_BOARD

    def expand(self):
        sub_size = 2 if len(self.state) % 2 == 0 else 3
        new_state = []
        for y in range(0, len(self.state), sub_size):
            new_rows = ['' for _ in range(sub_size + 1)]
            for x in range(0, len(self.state), sub_size):
                cell = [row[x:x+sub_size] for row in self.state[y:y+sub_size]]
                new_cell = self.rule_map['/'.join(cell)]
                for x in range(sub_size + 1):
                    new_rows[x] = f'{new_rows[x]}{new_cell[x]}'
            new_state.extend(new_rows)
        self.state = new_state

    def count_on(self):
        return sum(row.count('#') for row in self.state)


def parse_input(input: str):
    return [pattern.split('/') for pattern in input.strip().split(' => ')]


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def get_rule_map(rules: List[List[List[str]]]):
    rule_map = {}

    for input, output in rules:
        rule_map['/'.join(input)] = output
        rotated_input = input
        for _ in range(3):
            rotated_input = [''.join(row) for row in zip(*(list(row) for row in rotated_input[::-1]))]
            rule_map['/'.join(rotated_input)] = output

        flipped_input = input[::-1]
        rule_map['/'.join(flipped_input)] = output
        rotated_input = flipped_input
        for _ in range(3):
            rotated_input = [''.join(row) for row in zip(*(list(row) for row in rotated_input[::-1]))]
            rule_map['/'.join(rotated_input)] = output

    return rule_map


def part_1(override_inputs = None):
    rules = get_inputs(parse_input) if override_inputs is None else override_inputs
    rule_map = get_rule_map(rules)

    board = Board(rule_map)
    for _ in range(5):
        board.expand()

    return board.count_on()


def part_2(override_inputs = None):
    rules = get_inputs(parse_input) if override_inputs is None else override_inputs
    rule_map = get_rule_map(rules)

    board = Board(rule_map)
    for _ in range(18):
        board.expand()

    return board.count_on()


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
