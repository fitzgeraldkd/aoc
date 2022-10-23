import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def parse_input(input: str):
    return [int(address) for address in input.strip().split('-')]


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    blacklist = get_inputs()
    address = 0
    changed_address = True

    while changed_address:
        changed_address = False
        for start, end in blacklist:
            if start <= address and end >= address:
                changed_address = True
                address = end + 1
                break

    return address


def part_2():
    blacklist = get_inputs()
    whitelist_count = 0
    address = 0

    while address <= 4294967295:
        blacklisted = False
        for start, end in blacklist:
            if start <= address and end >= address:
                blacklisted = True
                address = end + 1
                break
        if not blacklisted:
            whitelist_count += 1
            address += 1

    return whitelist_count


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
