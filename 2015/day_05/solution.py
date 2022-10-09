import os
import re


def parse_input(input):
    return input


def get_inputs():
    # return [
    #     'qjhvhtzxzqqjkmpb',
    #     'xxyxx',
    #     'uurcxstgmygtbstg',
    #     'ieodomkazucvgmuy',
    #     'aaa'
    # ]
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    inputs = get_inputs()

    nice_string_count = 0
    for input in inputs:
        if re.search(r'(ab|cd|pq|xy)', input):
            continue
        if len(re.findall(r'[aeiou]', input)) < 3:
            continue
        if re.search(r'([a-z])\1', input) is None:
            continue

        nice_string_count += 1

    return nice_string_count


def part_2():
    inputs = get_inputs()

    nice_string_count = 0
    for input in inputs:
        print()
        print(input)
        # print(re.split(r'(([a-z]){2})', input))
        # print(re.findall(r'(([a-z])\2)', input))
        print(re.findall(r'([a-z]{2})(\w)*\1', input))
        # if re.findall(r'(([a-z])\2{1})\1{1}', input) is None:
        # if re.match(r'([a-z]{2})(\w)*\1{1}', input) is None:
        if len(re.findall(r'([a-z]{2})(\w)*\1', input)) > 0:
            # print(input)
            continue
        if re.search(r'([a-z])[a-z]\1', input) is None:
            # print(input)
            continue
        print('IN')
        nice_string_count += 1

    return nice_string_count


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())

'''
Part 2
0
[answer]
346
'''