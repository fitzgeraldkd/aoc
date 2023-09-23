import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def swap_positions(password: list, x: int, y: int):
    password[x], password[y] = password[y], password[x]


def swap_letters(password: list, x: str, y: str):
    for index, letter in enumerate(password):
        if letter == x:
            password[index] = y
        elif letter == y:
            password[index] = x


def rotate(password: list, amount: int):
    # Positive rotates to the right.
    amount = -1 * amount
    return [*password[amount:], *password[:amount]]


def reverse(password: list, x: int, y: int):
    reversed = password[x:y+1]
    reversed.reverse()
    for i in range(x, y+1):
        password[i] = reversed[i-x]


def move(password: list, x: int, y: int):
    letter = password.pop(x)
    password.insert(y, letter)


def parse_operation(operation: str, password: list, reversed = False):
    parts = operation.split(' ')
    if parts[0] == 'swap':
        if parts[1] == 'position':
            swap_positions(password, int(parts[2]), int(parts[5]))
        else:
            swap_letters(password, parts[2], parts[5])
    elif parts[0] == 'rotate':
        if parts[1] in ['left', 'right']:
            rotations = (int(parts[2]) % len(password)) * (-1 if reversed else 1)
            password = rotate(password, rotations * (1 if parts[1] == 'right' else -1))
        else:
            index = password.index(parts[6])
            if reversed:
                original = [*password]
                while original != parse_operation(operation, password):
                    password = rotate(password, 1)
            else:
                rotations = ((1 + index + (1 if index >= 4 else 0)) % len(password))
                password = rotate(password, rotations)
    elif parts[0] == 'reverse':
        reverse(password, int(parts[2]), int(parts[4]))
    elif parts[0] == 'move':
        x, y = int(parts[2]), int(parts[5])
        if reversed:
            x, y = y, x
        move(password, x, y)
    
    return password


def part_1():
    operations = get_inputs()
    password = list('abcdefgh')

    for operation in operations:
        password = parse_operation(operation, password)

    return ''.join(password)


def part_2():
    operations = get_inputs()
    operations.reverse()
    password = list('fbgdceah')

    for operation in operations:
        password = parse_operation(operation, password, reversed=True)

    return ''.join(password)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
