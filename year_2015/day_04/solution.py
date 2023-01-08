import hashlib

from utils.setup import read_inputs


def hash(input: str):
    return hashlib.md5(input.encode('utf-8')).hexdigest()

def parse_input(input: str):
    return input.strip()


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)][0]


def part_1(override_inputs: str = None):
    inputs = override_inputs or get_inputs()

    for i in range(10000000):
        hashed = hash(f'{inputs}{i}')
        if hashed.startswith('00000'):
            return i


def part_2(override_inputs: str = None):
    inputs = override_inputs or get_inputs()

    for i in range(10000000):
        hashed = hash(f'{inputs}{i}')
        if hashed.startswith('000000'):
            return i


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
