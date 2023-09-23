import numpy as np
import os


def parse_input(input: str):
    split_input = input.strip().split(' ')
    return { 
        'row': int(split_input[1][1:]),
        'num_positions': int(split_input[3]), 
        'start': int(split_input[-1][:-1]) 
    }


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def is_clear(disc: dict, time: int):
    return (time + disc['row'] + disc['start']) % disc['num_positions'] == 0


def get_increment(discs, time):
    positions = []
    for disc in discs:
        if is_clear(disc, time):
            positions.append(disc['num_positions'])
    return np.lcm.reduce(positions)


def part_1():
    discs = get_inputs()

    time = 0
    while any([not is_clear(disc, time) for disc in discs]):
        time += get_increment(discs, time)
    
    return time


def part_2():
    discs = get_inputs()
    discs.append({
        'row': len(discs) + 1,
        'num_positions': 11, 
        'start': 0 
    })

    time = 0
    while any([not is_clear(disc, time) for disc in discs]):
        time += get_increment(discs, time)
    
    return time


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
