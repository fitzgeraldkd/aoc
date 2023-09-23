import os
import sys

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


class Interpreter:
    def __init__(self, instructions: list, eggs: int, multiply = False):
        self.registers = { 'a': eggs, 'b': 0, 'c': 0, 'd': 0 }
        self.instructions = []
        for instruction in instructions:
            command, arguments = instruction.split(' ', 1)
            arguments = [arg if arg in 'abcd' else int(arg) for arg in arguments.split(' ')]
            self.instructions.append({
                'command': command,
                'arguments': arguments,
                'toggled': False
            })
        self.index = 0
        self.multiply = multiply
    
    def copy(self, x, y):
        if y in self.registers:
            self.registers[y] = self.registers.get(x, x)
        self.index += 1
    
    def increment(self, x):
        if self.multiply:
            # self.registers[x] *= 1
            self.registers[x] *= 2
            # self.registers[x] = self.registers[x] ** 2
            # self.registers[x] += 2
        else:
            self.registers[x] += 1
        self.index += 1
    
    def decrement(self, x):
        self.registers[x] -= 1
        self.index += 1
    
    def jump_if_not_zero(self, x, y):
        if self.registers.get(x, x) != 0:
            self.index += self.registers.get(y, y)
        else:
            self.index += 1
    
    def toggle(self, x):
        COMMANDS = {
            'cpy': 'jnz',
            'inc': 'dec',
            'dec': 'inc',
            'jnz': 'cpy',
            'tgl': 'inc'
        }
        toggled_index = self.index + self.registers.get(x, x)
        if toggled_index < len(self.instructions):
            self.instructions[toggled_index]['command'] = COMMANDS[self.instructions[toggled_index]['command']]
            # if not self.instructions[toggled_index]['toggled']:
            #     print('UNTOGGLING')
            # self.instructions[toggled_index]['toggled'] = not self.instructions[toggled_index]['toggled']
        self.index += 1

    def run_command(self):
        COMMANDS = {
            'cpy': self.copy,
            'inc': self.increment,
            'dec': self.decrement,
            'jnz': self.jump_if_not_zero,
            'tgl': self.toggle
        }
        COMMANDS_TOGGLED = {
            'cpy': self.jump_if_not_zero,
            'inc': self.decrement,
            'dec': self.increment,
            'jnz': self.copy,
            'tgl': self.increment
        }
        instruction = self.instructions[self.index]
        # print(instruction)
        # print(self.index, self.registers)
        # input()
        if instruction['toggled']:
            COMMANDS_TOGGLED[instruction['command']](*instruction['arguments'])
        else:
            COMMANDS[instruction['command']](*instruction['arguments'])

    def execute(self):
        while self.index < len(self.instructions):
            self.run_command()
        
        return self.registers['a']


def part_1():
    instructions = get_inputs()
    interpreter = Interpreter(instructions, 7)

    return interpreter.execute()


def part_2():
    instructions = get_inputs()
    interpreter = Interpreter(instructions, 12, multiply=False)

    return interpreter.execute()


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
