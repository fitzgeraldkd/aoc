import hashlib
import os
import re

hashed = {}

def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def get_hash(index: int, stretched: bool):
    if index in hashed:
        return hashed[index]
    else:
        hash = f'{get_inputs()}{index}'
        for _ in range(2017 if stretched else 1):
            hash = hashlib.md5(hash.encode('utf-8')).hexdigest()
        hashed[index] = hash
        return hash


def is_key(index: int, stretched = False):
    hash = get_hash(index, stretched)
    triplet_match = re.search(r'([0-9a-f])(\1){2}', hash)
    if triplet_match:
        for stream in range(1000):
            stream_hash = get_hash(index + stream + 1, stretched)
            if triplet_match.group(0)[0]*5 in stream_hash:
                return True
    return False


def part_1():
    indeces = []

    index = 0
    while len(indeces) < 64:
        if is_key(index):
            indeces.append(index)
        index += 1

    return indeces[-1]


def part_2():
    global hashed
    hashed = {}
    
    indeces = []

    index = 0
    while len(indeces) < 64:
        if is_key(index, stretched=True):
            indeces.append(index)
        index += 1

    return indeces[-1]


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
