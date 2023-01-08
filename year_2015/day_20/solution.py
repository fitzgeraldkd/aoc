import math

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)][0]


def part_1():
    target = get_inputs()
    factor_map = {}

    def get_factors(number):
        if number not in factor_map:
            factor_map[number] = set()
            for i in range(math.floor(number ** 0.5)):
                if number % (i + 1) == 0:
                    factor_map[number].add(i + 1)
                    factor_map[number].add(number / (i + 1))
        return factor_map[number]

    def calculate_presents(house):
        return sum(get_factors(house)) * 10

    house = 1
    while calculate_presents(house) < target:
        house += 1

    return house


def part_2():
    target = get_inputs()
    factor_map = {}
    elves = {}

    def get_factors(number):
        if number not in factor_map:
            factor_map[number] = set()
            for i in range(math.floor(number ** 0.5)):
                if number % (i + 1) == 0:
                    for factor in [i + 1, number / (i + 1)]:
                        if factor in elves:
                            if elves[factor] < 50:
                                elves[factor] += 1
                                factor_map[number].add(factor)
                        else:
                            elves[factor] = 1
                            factor_map[number].add(factor)
        return factor_map[number]

    def calculate_presents(house):
        return sum(get_factors(house)) * 11

    house = 1
    while calculate_presents(house) < target:
        house += 1

    return house


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
