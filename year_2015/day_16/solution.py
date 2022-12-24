import os


def parse_input(input: str):
    [name, traits] = input.strip().split(': ', 1)
    sue = { 'id': int(name.split(' ')[1]) }
    for trait in traits.split(', '):
        [trait_name, quantity] = trait.split(': ')
        sue[trait_name] = int(quantity)
    return sue


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


FILTERS = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}


def part_1():
    sues = get_inputs()

    def matches_property(sue, trait, quantity):
        if trait not in sue:
            return True
        
        return sue[trait] == quantity

    for trait in FILTERS.keys():
        sues = list(filter(lambda sue: matches_property(sue, trait, FILTERS[trait]), sues))

    return sues[0]['id']


def part_2():
    sues = get_inputs()

    def matches_property(sue, trait, quantity):
        if trait not in sue:
            return True
        elif trait in ['cats', 'trees']:
            return sue[trait] > quantity
        elif trait in ['pomeranians', 'goldfish']:
            return sue[trait] < quantity
        else:
            return sue[trait] == quantity
    
    for trait in FILTERS.keys():
        sues = list(filter(lambda sue: matches_property(sue, trait, FILTERS[trait]), sues))

    return sues[0]['id']


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
