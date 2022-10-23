import os


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def part_1():
    instructions = get_inputs()

    registers = { 'a': 0, 'b': 0, 'c': 0, 'd': 0 }

    index = 0
    while index < len(instructions):
        instruction = instructions[index]
        if instruction.startswith('cpy'):
            _, src, rec = instruction.split(' ')
            registers[rec] = registers[src] if src in registers else int(src)
        elif instruction.startswith('inc'):
            registers[instruction[-1]] += 1
        elif instruction.startswith('dec'):
            registers[instruction[-1]] -= 1
        elif instruction.startswith('jnz'):
            _, val, amt = instruction.split(' ')
            val = registers[val] if val in registers else int(val)
            if val != 0:
                index += int(amt)
                continue
        index += 1


    return registers['a']


def part_2():
    instructions = get_inputs()

    registers = { 'a': 0, 'b': 0, 'c': 1, 'd': 0 }

    index = 0
    while index < len(instructions):
        instruction = instructions[index]
        if instruction.startswith('cpy'):
            _, src, rec = instruction.split(' ')
            registers[rec] = registers[src] if src in registers else int(src)
        elif instruction.startswith('inc'):
            registers[instruction[-1]] += 1
        elif instruction.startswith('dec'):
            registers[instruction[-1]] -= 1
        elif instruction.startswith('jnz'):
            _, val, amt = instruction.split(' ')
            val = registers[val] if val in registers else int(val)
            if val != 0:
                index += int(amt)
                continue
        index += 1


    return registers['a']


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
