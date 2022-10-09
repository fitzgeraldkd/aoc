import hashlib
import os


def hash(input: str):
    return hashlib.md5(input.encode('utf-8')).hexdigest()

def parse_input(input):
    return input


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def part_1():
    inputs = get_inputs()

    for i in range(1000000):
        hashed = hash(f'{inputs}{i}')
        if hashed.startswith('00000'):
            return i

    return None


def part_2():
    inputs = get_inputs()

    for i in range(10000000):
        hashed = hash(f'{inputs}{i}')
        if hashed.startswith('000000'):
            return i

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
