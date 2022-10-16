import hashlib
import os


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def part_1():
    door_id = get_inputs()

    password = []
    index = 0
    while len(password) < 8:
        hash = hashlib.md5(f'{door_id}{index}'.encode('utf-8')).hexdigest()

        if (hash).startswith('00000'):
            password.append(hash[5])

        index += 1

    return ''.join(password)


def part_2():
    door_id = get_inputs()

    password = [None, None, None, None, None, None, None, None]
    index = 0
    while any([character is None for character in password]):
        hash = hashlib.md5(f'{door_id}{index}'.encode('utf-8')).hexdigest()

        if (hash).startswith('00000') and hash[5] not in ['a', 'b', 'c', 'd', 'e', 'f']:

            position = int(hash[5])
            if position < len(password) and password[position] is None:
                password[position] = hash[6]

        index += 1

    return ''.join(password)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
