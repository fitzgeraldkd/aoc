import os


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs[0]


def decompress(file: str):
    decompressed_file = []
    index = 0
    while index < len(file):
        if file[index] == '(':
            closing_index = file[index:].index(')') + index
            length, count = [int(value) for value in file[index+1:closing_index].split('x')]
            substring = file[closing_index+1:closing_index+length+1]
            decompressed_file.append(substring * count)
            index = closing_index + length + 1
        else:
            decompressed_file.append(file[index])
            index += 1
    return ''.join(decompressed_file)


def part_1():
    file = get_inputs()

    decompressed_file = decompress(file)
    
    return len(decompressed_file)


def decompress_recursive(file: str):
    index = 0
    size = 0
    while index < len(file):
        if file[index] == '(':
            close_index = file.index(')', index)
            length, count = [int(value) for value in file[index+1:close_index].split('x')]

            size += decompress_recursive(file[close_index+1:close_index+length+1]) * count

            index = close_index + length + 1
        else:
            index += 1
            size += 1

    return size


def part_2():
    file = get_inputs()

    decompressed_file = decompress_recursive(file)
    
    return decompressed_file


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
