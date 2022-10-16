import os


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    inputs = get_inputs()

    KEYPAD = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    code = []

    x = 1
    y = 1
    for input in inputs:
        for direction in input:
            if direction == 'U':
                y = max(y-1, 0)
            elif direction == 'D':
                y = min(y+1, 2)
            elif direction == 'L':
                x = max(x-1, 0)
            elif direction == 'R':
                x = min(x+1, 2)
        code.append(KEYPAD[y][x])

    return ''.join(code)


def part_2():
    inputs = get_inputs()

    KEYPAD = [
        [None, None, '1', None, None],
        [None, '2', '3', '4', None],
        ['5', '6', '7', '8', '9'],
        [None, 'A', 'B', 'C', None],
        [None, None, 'D', None, None]
    ]

    code = []

    x = 0
    y = 2
    for input in inputs:
        for direction in input:
            if direction == 'U' and y > 0:
                new_y = y - 1
                if KEYPAD[new_y][x] is not None:
                    y = new_y
            elif direction == 'D' and y < 4:
                new_y = y + 1
                if KEYPAD[new_y][x] is not None:
                    y = new_y
            elif direction == 'L' and x > 0:
                new_x = x - 1
                if KEYPAD[y][new_x] is not None:
                    x = new_x
            elif direction == 'R' and x < 4:
                new_x = x + 1
                if KEYPAD[y][new_x] is not None:
                    x = new_x
        code.append(KEYPAD[y][x])

    return ''.join(code)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
