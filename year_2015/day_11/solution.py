import re

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)][0]


def increment_character(input):
    output = chr((ord(input) - ord('a') + 1) % 26 + ord('a'))
    output = replace_illegal_characters(output)
    return (output, output == 'a')

def increment_password(password):
    password_list = list(password)
    index = len(password_list) - 1
    while index >= 0:
        new_character, wrapped = increment_character(password_list[index])
        password_list[index] = new_character
        index -= 1
        if not wrapped:
            break
    return ''.join(password_list)

def replace_illegal_characters(input):
    output = re.sub('i', 'j', input)
    output = re.sub('l', 'm', output)
    output = re.sub('o', 'p', output)
    return output

def passes_rules(input):
    if re.search(r'[ilo]', input):
        return False

    if len(set(re.findall(r'([a-z])\1', input))) < 2:
        return False

    previous_char = input[0]
    streak = 0
    for char in input[1:]:
        if ord(char) - ord(previous_char) == 1:
            streak += 1
        else:
            streak = 0

        if streak == 2:
            return True

        previous_char = char

    return False


def part_1():
    inputs = get_inputs()

    output = increment_password(inputs)

    while not passes_rules(output):
        output = increment_password(output)

    return output


def part_2():
    inputs = part_1()

    output = increment_password(inputs)

    while not passes_rules(output):
        output = increment_password(output)

    return output


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
