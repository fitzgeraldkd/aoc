from typing import Callable, List

from utils.setup import read_inputs


STARTING_LINE = 'abcdefghijklmnop'


def parse_input(input: str):
    return input.strip().split(',')


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)][0]


def move(line: List[str], instruction: str):
    if instruction[0] == 's':
        amount = -1 * int(instruction[1:])
        return line[amount:] + line[:amount]
    elif instruction[0] == 'x':
        a, b = [int(position) for position in instruction[1:].split('/')]
        # line[a], line[b] = line[a], line[b]
    elif instruction[0] == 'p':
        a, b = instruction[1:].split('/')
        a = line.index(a)
        b = line.index(b)
    line[a], line[b] = line[b], line[a]
    return line


def part_1(override_inputs: List[str] = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    line = list(STARTING_LINE)
    for instruction in instructions:
        line = move(line, instruction)

    return ''.join(line)


def part_2(override_inputs: List[str] = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs

    line = list(STARTING_LINE)
    checked_lines = { ''.join(line): 0 }

    number_of_dances = 1000000000

    current_dance_number = 0
    is_last_cycle = False
    while current_dance_number < number_of_dances:
        for instruction in instructions:
            line = move(line, instruction)
        line_string = ''.join(line)
        current_dance_number += 1

        if not is_last_cycle:
            if line_string in checked_lines:
                first_occurrence = checked_lines[line_string]
                cycle_length = current_dance_number - first_occurrence
                cycles_to_skip = (number_of_dances - current_dance_number) // cycle_length
                current_dance_number += (cycle_length * cycles_to_skip)
                is_last_cycle = True
            else:
                checked_lines[line_string] = current_dance_number

    return ''.join(line)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
