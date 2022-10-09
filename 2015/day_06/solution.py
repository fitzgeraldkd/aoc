import os
import re


def parse_input(input: str):
    split_input = re.split(r'(turn on|turn off|toggle)', input.strip())
    coordinates = [[int(val) for val in coordinate.split(',')] for coordinate in split_input[2].split(' through ')]
    return {
        'action': split_input[1],
        'coordinates': {
            'start': coordinates[0],
            'end': coordinates[1]
        }
    }


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    inputs = get_inputs()

    lights = [[False for _ in range(1000)] for _ in range(1000)]

    for input in inputs:
        for x in range(input['coordinates']['start'][0], input['coordinates']['end'][0]+1):
            for y in range(input['coordinates']['start'][1], input['coordinates']['end'][1]+1):
                if input['action'] == 'turn on':
                    lights[x][y] = True
                elif input['action'] == 'turn off':
                    lights[x][y] = False
                else:
                    lights[x][y] = not lights[x][y]


    lights_on = 0
    for row in lights:
        for light in row:
            lights_on += 1 if light else 0

    return lights_on


def part_2():
    inputs = get_inputs()

    lights = [[0 for _ in range(1000)] for _ in range(1000)]

    for input in inputs:
        for x in range(input['coordinates']['start'][0], input['coordinates']['end'][0]+1):
            for y in range(input['coordinates']['start'][1], input['coordinates']['end'][1]+1):
                if input['action'] == 'turn on':
                    lights[x][y] += 1
                elif input['action'] == 'turn off':
                    lights[x][y] -= 1 if lights[x][y] > 0 else 0
                else:
                    lights[x][y] += 2


    intensity = 0
    for row in lights:
        for light in row:
            intensity += light

    return intensity


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
