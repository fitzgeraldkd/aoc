import os


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def expand_data(data: str):
    data_to_append = data[::-1].replace('1', '_').replace('0', '1').replace('_', '0')
    return f'{data}0{data_to_append}'


def get_checksum(data: str):
    checksum = []
    for pair in [data[i:i+2] for i in range(0, len(data), 2)]:
        checksum.append('1' if pair[0] == pair[1] else '0')
    checksum = ''.join(checksum)
    return checksum if len(checksum) % 2 == 1 else get_checksum(checksum)


def part_1():
    data = get_inputs()

    while len(data) < 272:
        data = expand_data(data)

    data = data[:272]

    return get_checksum(data)


def part_2():
    data = get_inputs()

    while len(data) < 35651584:
        data = expand_data(data)

    data = data[:35651584]

    return get_checksum(data)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
