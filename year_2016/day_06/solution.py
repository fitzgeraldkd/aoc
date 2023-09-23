import math
import os


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    inputs = get_inputs()

    letter_counts = [{} for _ in range(len(inputs[0]))]

    for input in inputs:
        for index, letter in enumerate(input):
            if letter in letter_counts[index]:
                letter_counts[index][letter] += 1
            else:
                letter_counts[index][letter] = 1
    
    message = []
    for letter_count in letter_counts:
        next_letter = None
        count = 0
        for letter in letter_count:
            if letter_count[letter] > count:
                next_letter = letter
                count = letter_count[letter]
        message.append(next_letter)

    return ''.join(message)


def part_2():
    inputs = get_inputs()

    letter_counts = [{} for _ in range(len(inputs[0]))]

    for input in inputs:
        for index, letter in enumerate(input):
            if letter in letter_counts[index]:
                letter_counts[index][letter] += 1
            else:
                letter_counts[index][letter] = 1
    
    message = []
    for letter_count in letter_counts:
        next_letter = None
        count = math.inf
        for letter in letter_count:
            if letter_count[letter] < count:
                next_letter = letter
                count = letter_count[letter]
        message.append(next_letter)

    return ''.join(message)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
