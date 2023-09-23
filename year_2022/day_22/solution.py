import operator
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.lists import split
from utils.pathing import rotate
from utils.setup import read_inputs


FACE_SIZE = 50

BOX_PATTERNS = {
    #  ..
    #  .
    # ..
    # .
    ((1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (0, 3)): {
        # key = face coordinate
        (1, 0): {
            # key = direction leaving face
            (0, -1): {
                'get_position': lambda position: (0, (FACE_SIZE * 3) + (position[0] % FACE_SIZE)),
                'facing': (1, 0)
            },
            (-1, 0): {
                'get_position': lambda position: (0, (FACE_SIZE * 3 - 1) - (position[1] % FACE_SIZE)),
                'facing': (1, 0)
            }
        },
        (2, 0): {
            (0, -1): {
                'get_position': lambda position: (position[0] % FACE_SIZE, FACE_SIZE * 4 - 1),
                'facing': (0, -1)
            },
            (1, 0): {
                'get_position': lambda position: (FACE_SIZE * 2 - 1, (FACE_SIZE * 3 - 1) - (position[1] % FACE_SIZE)),
                'facing': (-1, 0)
            },
            (0, 1): {
                'get_position': lambda position: (FACE_SIZE * 2 - 1, FACE_SIZE + position[0] % FACE_SIZE),
                'facing': (-1, 0)
            }
        },
        (1, 1): {
            # key = direction leaving face
            (-1, 0): {
                'get_position': lambda position: (position[1] % FACE_SIZE, FACE_SIZE * 2),
                'facing': (0, 1)
            },
            (1, 0): {
                'get_position': lambda position: (FACE_SIZE * 2 + (position[1] % FACE_SIZE), FACE_SIZE - 1),
                'facing': (0, -1)
            }
        },
        (0, 2): {
            # key = direction leaving face
            (-1, 0): {
                'get_position': lambda position: (FACE_SIZE, FACE_SIZE - 1 - (position[1] % FACE_SIZE)),
                'facing': (1, 0)
            },
            (0, -1): {
                'get_position': lambda position: (FACE_SIZE, FACE_SIZE + (position[0] % FACE_SIZE)),
                'facing': (1, 0)
            }
        },
        (1, 2): {
            # key = direction leaving face
            (1, 0): {
                'get_position': lambda position: (FACE_SIZE * 3 - 1, FACE_SIZE - 1 - (position[1] % FACE_SIZE)),
                'facing': (-1, 0)
            },
            (0, 1): {
                'get_position': lambda position: (FACE_SIZE - 1, FACE_SIZE * 3 + (position[0] % FACE_SIZE)),
                'facing': (-1, 0)
            }
        },
        (0, 3): {
            (1, 0): {
                'get_position': lambda position: (FACE_SIZE + (position[1] % FACE_SIZE), FACE_SIZE * 3 - 1),
                'facing': (0, -1)
            },
            (0, 1): {
                'get_position': lambda position: (FACE_SIZE * 2 + (position[0] % FACE_SIZE), 0),
                'facing': (0, 1)
            },
            (-1, 0): {
                'get_position': lambda position: (FACE_SIZE + (position[1] % FACE_SIZE), 0),
                'facing': (0, 1)
            }
        }
    }
}


def parse_input(input: str):
    return input.rstrip()
    return int(input.strip())


def get_inputs(parser: Callable):
    inputs = read_inputs(__file__)
    # inputs = read_inputs(__file__, 'sample.txt')
    layout, directions = split(inputs, '\n')
    directions = ' R '.join(directions[0].strip().split('R'))
    directions = ' L '.join(directions.split('L'))
    directions = directions.split(' ')
    directions = [(instruction if instruction in ['L', 'R'] else int(instruction)) for instruction in directions]
    # print(directions)
    return [parser(line) for line in layout], directions
    # return [parser(line) for line in read_inputs(__file__)]
    return [parser(line) for line in read_inputs(__file__, 'sample.txt')]


def add_distance(layout: list, position, facing, distance):
    new_x = position[0] + facing[0]
    new_y = position[1] + facing[1]
    if facing[0] != 0:
        min_y = next([i for i in range(len(layout)) if len(layout[i]) > new_x and layout[i][new_x] == '.'])
        max_y = next([i for i in range(len(layout) - 1, -1, -1) if len(layout[i]) > new_x and layout[i][new_x] == '.'])
        if new_y > max_y:
            new_y = min_y
    else:
        pass


def steps_to_rock(layout, position, facing):
    pass


def get_limits(layout):
    row_limits = {}
    col_limits = {}

    max_line_length = 0

    for y, row in enumerate(layout):
        row_limits[y] = { 'min': len(row) - len(row.strip()), 'max': len(row) - 1 }
        max_line_length = max(max_line_length, len(row))

    for x in range(max_line_length):
        min_y = next(i for i in range(len(layout)) if len(layout[i]) > x and layout[i][x] != ' ')
        max_y = next(i for i in range(len(layout) - 1, -1, -1) if len(layout[i]) > x and layout[i][x] != ' ')
        col_limits[x] = { 'min': min_y, 'max': max_y}

    return row_limits, col_limits


def part_1(override_inputs = None):
    layout, directions = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = None
    position = (layout[0].index('.'), 0)
    facing = (1, 0)

    row_limits, col_limits = get_limits(layout)
    # print(row_limits)
    # print(col_limits)
    # print(directions)

    for instruction in directions:
        # print(instruction)
        if instruction in ['L', 'R']:
            facing = rotate(facing, instruction)
        else:
            # print(position, facing)
            for _ in range(instruction):
                # if instruction == 10:
                #     print('test', position)
                new_x = position[0] + facing[0]
                new_y = position[1] + facing[1]
                if new_x > row_limits[position[1]]['max']:
                    new_x = row_limits[position[1]]['min']
                elif new_x < row_limits[position[1]]['min']:
                    new_x = row_limits[position[1]]['max']
                elif new_y > col_limits[position[0]]['max']:
                    new_y = col_limits[position[0]]['min']
                elif new_y < col_limits[position[0]]['min']:
                    new_y = col_limits[position[0]]['max']

                if layout[new_y][new_x] == '#':
                    # print('ROCK', new_x, new_y)
                    break

                position = (new_x, new_y)


    facing_points = {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3
    }

    return 1000 * (position[1] + 1) + 4 * (position[0] + 1) + facing_points[facing]


def part_2(override_inputs = None):
    # layout, directions = get_inputs(parse_input) if override_inputs is None else override_inputs
    # output = None

    # faces = {}
    # for y in range(0, len(layout), 50):
    #     for x in range(0, len(layout[y]), 50):
    #         if layout[y][x] != ' ':
    #             faces[(x // 50, y // 50)] = [line[x:x + 50] for line in layout[y:y + 50]]

    # for face in faces:
    #     print()
    #     print(face)
    #     print(faces[face])



    # return output
    layout, directions = get_inputs(parse_input) if override_inputs is None else override_inputs
    output = None
    position = (layout[0].index('.'), 0)
    facing = (1, 0)

    row_limits, col_limits = get_limits(layout)
    # print(row_limits)
    # print(col_limits)
    # print(directions)
    box_pattern = list(BOX_PATTERNS.values())[0]

    for index, instruction in enumerate(directions):
        # print(instruction)
        if instruction in ['L', 'R']:
            facing = rotate(facing, instruction)
        else:
            # print(position, facing)
            for d in range(instruction):
                # if instruction == 10:
                #     print('test', position)
                new_x = position[0] + facing[0]
                new_y = position[1] + facing[1]
                new_facing = facing
                if new_x > row_limits[position[1]]['max'] or new_x < row_limits[position[1]]['min'] or new_y > col_limits[position[0]]['max'] or new_y < col_limits[position[0]]['min']:
                    face_leaving = box_pattern[(position[0] // FACE_SIZE, position[1] // FACE_SIZE)]
                    new_x, new_y = face_leaving[facing]['get_position'](position)
                    new_facing = face_leaving[facing]['facing']
                    print()
                    print('CHANGING FACES:')
                    print(position)
                    print((new_x, new_y))
                    print('facing', new_facing)
                    # print(directions[index:])
                    # print((new_x, new_y), d)
                    # return

                if layout[new_y][new_x] == '#':
                    # print('ROCK', new_x, new_y)
                    break

                position = (new_x, new_y)
                # position = new_position
                facing = new_facing

    facing_points = {
        (1, 0): 0,
        (0, 1): 1,
        (-1, 0): 2,
        (0, -1): 3
    }

    return 1000 * (position[1] + 1) + 4 * (position[0] + 1) + facing_points[facing]
    # position = (0, 150 + (58 % 50))
    # print(layout[position[1]][position[0]])
    # facing = (1, 0)
    # for index, instruction in enumerate(directions):
    #     # print(instruction)
    #     if instruction in ['L', 'R']:
    #         facing = rotate(facing, instruction)
    #     else:
    #         # print(position, facing)
    #         for d in range(instruction):
    #             # if instruction == 10:
    #             #     print('test', position)
    #             new_x = position[0] + facing[0]
    #             new_y = position[1] + facing[1]
    #             if new_x > row_limits[position[1]]['max'] or new_x < row_limits[position[1]]['min'] or new_y > col_limits[position[0]]['max'] or new_y < col_limits[position[0]]['min']:
    #                 print(directions[index:])
    #                 print((new_x, new_y), d)
    #                 return

    #             if layout[new_y][new_x] == '#':
    #                 # print('ROCK', new_x, new_y)
    #                 break

    #             position = (new_x, new_y)

    # position = (100 + 34 % 50, 0)
    # print(layout[position[1]][position[0]])
    # facing = (0, 1)
    # for index, instruction in enumerate(directions):
    #     # print(instruction)
    #     if instruction in ['L', 'R']:
    #         facing = rotate(facing, instruction)
    #     else:
    #         # print(position, facing)
    #         for d in range(instruction):
    #             # if instruction == 10:
    #             #     print('test', position)
    #             new_x = position[0] + facing[0]
    #             new_y = position[1] + facing[1]
    #             if new_x > row_limits[position[1]]['max'] or new_x < row_limits[position[1]]['min'] or new_y > col_limits[position[0]]['max'] or new_y < col_limits[position[0]]['min']:
    #                 print(directions[index:])
    #                 print((new_x, new_y), d)
    #                 return

    #             if layout[new_y][new_x] == '#':
    #                 # print('ROCK', new_x, new_y)
    #                 break

    #             position = (new_x, new_y)

    # facing_points = {
    #     (1, 0): 0,
    #     (0, 1): 1,
    #     (-1, 0): 2,
    #     (0, -1): 3
    # }

    # return 1000 * (position[1] + 1) + 4 * (position[0] + 1) + facing_points[facing]


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
