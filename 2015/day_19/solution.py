import os
import re
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    molecule = inputs.pop()
    inputs.pop()
    replacements = [replacement.split(' => ') for replacement in inputs]
    return (replacements, molecule)


def part_1():
    (replacements, molecule) = get_inputs()
    molecules = set()

    for replacement in replacements:
        matches = list(re.finditer(replacement[0], molecule))
        for match in matches:
            molecules.add(molecule[:match.start()] + replacement[1] + molecule[match.end():])

    return len(molecules)


def part_2():
    (replacements, target) = get_inputs()
    queue = PriorityQueue()
    queue.add_item(target, len(target))

    steps = 0
    checked_molecules = set()
    while not queue.is_empty():
        steps += 1
        molecule = queue.pop()
        checked_molecules.add(molecule)

        for replacement in replacements:
            matches = list(re.finditer(replacement[1], molecule))
            for match in matches:
                new_molecule = molecule[:match.start()] + replacement[0] + molecule[match.end():]
                if new_molecule in checked_molecules:
                    continue
                if new_molecule == 'e':
                    return steps
                queue.add_item(new_molecule, len(new_molecule))


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())