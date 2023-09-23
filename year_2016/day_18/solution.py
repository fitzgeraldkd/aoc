import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

TRAP_CONDITIONS = [
    '^^.',
    '.^^',
    '^..',
    '..^'
]


def parse_input(input: str):
    return input.strip()


def get_inputs():
    # return '.^^.^.^^^^'
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def get_next_row(board: list):
    last_row = board[-1]
    new_row = []
    for i in range(len(last_row)):
        checks = []
        for j in [-1, 0, 1]:
            if i + j < 0 or i + j >= len(last_row):
                checks.append('.')
            else:
                checks.append(last_row[i+j])
        new_row.append('^' if ''.join(checks) in TRAP_CONDITIONS else '.')
    return ''.join(new_row)


def get_safe_tiles(board: list):
    safe_tiles = 0
    for row in board:
        for tile in row:
            safe_tiles += 1 if tile == '.' else 0
    return safe_tiles


def part_1():
    board = [get_inputs()]

    while len(board) < 40:
        board.append(get_next_row(board))

    return get_safe_tiles(board)


def part_2():
    row = get_inputs()

    safe_tiles = 0
    rows_counted = 0

    # TODO: Check if the pattern repeats.

    while rows_counted < 400000:
        safe_tiles += get_safe_tiles([row])
        row = get_next_row([row])
        rows_counted += 1

    return safe_tiles


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
