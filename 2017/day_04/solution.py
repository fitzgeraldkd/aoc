import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip().split(' ')


def get_inputs():
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parse_input(line) for line in read_inputs(script_directory)]


def part_1(override_inputs: list = None):
    passphrases = get_inputs() if override_inputs is None else override_inputs
    valid_count = 0

    for passphrase in passphrases:
        if len(passphrase) == len(set(passphrase)):
            valid_count += 1

    return valid_count


def part_2(override_inputs: list = None):
    passphrases = get_inputs() if override_inputs is None else override_inputs
    valid_count = 0

    for passphrase in passphrases:
        passphrase = [''.join(sorted(word)) for word in passphrase]
        if len(passphrase) == len(set(passphrase)):
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
