from utils.setup import read_inputs


def parse_input(input: str):
    return input.strip()


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)][0]


def look_and_say(input: str):
    count = 0
    previous = None
    output = ''

    for char in input:
        if previous is None or char == previous:
            previous = char
            count += 1
        else:
            output += str(count) + previous
            previous = char
            count = 1

    output += str(count) + previous

    return output


def part_1():
    inputs = get_inputs()

    output = inputs
    for _ in range(40):
        output = look_and_say(output)

    return len(output)


def part_2():
    inputs = get_inputs()

    output = inputs
    for _ in range(50):
        output = look_and_say(output)

    return len(output)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
