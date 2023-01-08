from utils.setup import read_inputs


TARGET_VOLUME = 150


def parse_input(input: str):
    return int(input.strip())


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def count_permutations(containers, target, depth, solutions):
    containers = list(filter(lambda container: container <= target, containers))

    for i in range(len(containers)):
        if containers[i] == target:
            if depth in solutions:
                solutions[depth] += 1
            else:
                solutions[depth] = 1
        else:
            solutions = count_permutations(containers[i+1:], target - containers[i], depth + 1, solutions)

    return solutions


def part_1():
    inputs = get_inputs()

    solutions = count_permutations(inputs, TARGET_VOLUME, 1, {})

    return sum(solutions.values())


def part_2():
    inputs = get_inputs()

    solutions = count_permutations(inputs, TARGET_VOLUME, 1, {})

    return solutions[min(solutions.keys())]


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
