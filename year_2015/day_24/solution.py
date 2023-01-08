from functools import reduce
import math

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip())


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def get_permutations(weights, target, permutations=[], partial=[]):
    for index, weight in enumerate(weights):
        if sum(partial) + weight == target:
            permutations.append([*partial, weight])
        elif sum(partial) + weight < target:
            get_permutations(weights[index+1:], target, permutations, [*partial, weight])
    return permutations

def part_1():
    inputs = get_inputs()
    sleigh_weight = int(sum(inputs) / 3)

    permutations = get_permutations(inputs, sleigh_weight)

    min_count = math.inf
    min_quantum_entanglement = math.inf

    for permutation in permutations:
        if len(permutation) < min_count:
            min_count = len(permutation)
            # min_quantum_entanglement = math.prod(permutation)
            min_quantum_entanglement = reduce(lambda a, b: a * b, permutation)
        elif len(permutation) == min_count:
            # min_quantum_entanglement = min(min_quantum_entanglement, math.prod(permutation))
            min_quantum_entanglement = min(min_quantum_entanglement, reduce(lambda a, b: a * b, permutation))

    return min_quantum_entanglement


def part_2():
    inputs = get_inputs()
    sleigh_weight = int(sum(inputs) / 4)

    permutations = get_permutations(inputs, sleigh_weight)

    min_count = math.inf
    min_quantum_entanglement = math.inf

    for permutation in permutations:
        if len(permutation) < min_count:
            min_count = len(permutation)
            # min_quantum_entanglement = math.prod(permutation)
            min_quantum_entanglement = reduce(lambda a, b: a * b, permutation)
        elif len(permutation) == min_count:
            # min_quantum_entanglement = min(min_quantum_entanglement, math.prod(permutation))
            min_quantum_entanglement = min(min_quantum_entanglement, reduce(lambda a, b: a * b, permutation))

    return min_quantum_entanglement


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
