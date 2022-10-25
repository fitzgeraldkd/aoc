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
    def __init__(self, instructions: list, initial: int):
        self.registers = { 'a': initial, 'b': 0, 'c': 0, 'd': 0 }
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
        self.sequence = []
        self.failed = False
    
    def copy(self, x, y):
        if y in self.registers:
            self.registers[y] = self.registers.get(x, x)
        self.index += 1
    
    def increment(self, x):
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
    
    def out(self, x):
        value = self.registers.get(x, x)
        if len(self.sequence) == 0 and value == 0:
            self.sequence.append(value)
        elif len(self.sequence) > 0:
            if value in [0, 1] and value != self.sequence[-1]:
                self.sequence.append(value)
            else:
                self.failed = True
        else:
            self.failed = True
        self.index += 1

    def run_command(self):
        COMMANDS = {
            'cpy': self.copy,
            'inc': self.increment,
            'dec': self.decrement,
            'jnz': self.jump_if_not_zero,
            'out': self.out
        }
        instruction = self.instructions[self.index]
        COMMANDS[instruction['command']](*instruction['arguments'])

    def execute(self):
        while not self.failed and self.index < len(self.instructions) and len(self.sequence) < 1000:
            self.run_command()
        return self.sequence == [i % 2 for i in range(1000)]
        return self.registers['a']


def part_1():
    instructions = get_inputs()
    initial = 196
    while True:
        print(initial)
        interpreter = Interpreter(instructions, initial)
        success = interpreter.execute()
        if success:
            return initial
        else:
            initial += 1


def part_2():
    inputs = get_inputs()

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
