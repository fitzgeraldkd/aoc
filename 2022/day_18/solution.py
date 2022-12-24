import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.pathing import get_adjacent_3d
from utils.setup import read_inputs


def parse_input(input: str):
    return tuple(int(value) for value in input.strip().split(','))


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]

def get_surface_area(cubes):

    faces = set()
    duplicate = set()

    for x, y, z in cubes:
        potential_faces = [
            ((x, y, z), (x + 1, y + 1, z)),
            ((x, y, z + 1), (x + 1, y + 1, z + 1)),
            ((x, y, z), (x + 1, y, z + 1)),
            ((x, y + 1, z), (x + 1, y + 1, z + 1)),
            ((x, y, z), (x, y + 1, z + 1)),
            ((x + 1, y, z), (x + 1, y + 1, z + 1))
        ]
        for face in potential_faces:
            if face in faces:
                duplicate.add(face)
                faces.remove(face)
            elif face not in duplicate:
                faces.add(face)

    return len(faces)


def part_1(override_inputs = None):
    cubes = get_inputs(parse_input) if override_inputs is None else override_inputs
    return get_surface_area(cubes)


def backfill(cube_states, cube, checked_cubes: set):
    """
    The open air fills in from one direction, so depending on the arrangement it may be required to backfill by
    replacing any adjacent undetermined blocks.
    """
    for x, y, z in [neighbor for neighbor in get_adjacent_3d(cube)
                    if neighbor not in checked_cubes and cube_states.get(neighbor, False) is None]:
        cube_states[(x, y, z)] = 'OPEN'
        backfill(cube_states, (x, y, z), { *checked_cubes, (x, y, z) })


def part_2(override_inputs = None):
    cubes = get_inputs(parse_input) if override_inputs is None else override_inputs
    cubes = set(cubes)

    min_x, min_y, min_z = [min(cubes, key=lambda cube: cube[i])[i] for i in range(3)]
    max_x, max_y, max_z = [max(cubes, key=lambda cube: cube[i])[i] for i in range(3)]
    cube_states = {}

    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            for z in range(min_z, max_z + 1):
                if (x, y, z) in cubes:
                    cube_states[(x, y, z)] = 'CUBE'
                elif x in [min_x, max_x] or y in [min_y, max_y] or z in [min_z, max_z] \
                        or any([cube_states.get(adjacent) == 'OPEN' for adjacent in get_adjacent_3d((x, y, z))]):
                    cube_states[(x, y, z)] = 'OPEN'
                    backfill(cube_states, (x, y, z), set((x, y, z)))
                else:
                    cube_states[(x, y, z)] = None

    blocked_cubes = [cube for cube, state in cube_states.items() if state is None]

    return get_surface_area(cubes) - get_surface_area(blocked_cubes)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
