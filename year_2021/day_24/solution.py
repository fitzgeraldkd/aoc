import math
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from classes.PriorityQueue import PriorityQueue
from utils.setup import read_inputs

AMPHIPODS = 'ABCD'

def parse_input(input: str):
    return input.strip()


def get_inputs(parser: Callable):
    return [parser(line).split(' ') for line in read_inputs(__file__)]


class LogicUnit:
    def __init__(self, instructions, model_number):
        self.instructions = instructions
        self.model_number = model_number
        self.registers = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
        }
    
    def reset_registers(self):
        self.registers = {
            'w': 0,
            'x': 0,
            'y': 0,
            'z': 0,
        }
    
    def get_argument_value(self, argument):
        value = self.registers.get(argument)
        if value is None:
            value = int(argument)
        return value
    
    def input(self, register, value):
        self.registers[register] = value
    
    def add(self, register, amount):
        self.registers[register] += self.get_argument_value(amount)
    
    def multiply(self, register, amount):
        self.registers[register] *= self.get_argument_value(amount)
    
    def divide(self, register, amount):
        self.registers[register] /= self.get_argument_value(amount)

    def modulo(self, register, amount):
        self.registers[register] %= self.get_argument_value(amount)
    
    def equals(self, register, amount):
        self.registers[register] = 1 if self.registers[register] == self.get_argument_value(amount) else 0

    def check_is_valid(self):
        digits = [*self.model_number]
        for instruction in self.instructions:
            if instruction[0] == 'inp':
                self.input(instruction[1], digits.pop(0))
            elif instruction[0] == 'add':
                self.add(*instruction[1:])
            elif instruction[0] == 'mul':
                self.multiply(*instruction[1:])
            elif instruction[0] == 'div':
                try:
                    self.divide(*instruction[1:])
                except ZeroDivisionError:
                    return False, len(self.model_number) - len(digits) - 1
            elif instruction[0] == 'mod':
                if self.registers[instruction[1]] < 0 or self.get_argument_value(instruction[2]) <= 0:
                    return False, len(self.model_number) - len(digits) - 1
                self.modulo(*instruction[1:])
            elif instruction[0] == 'eql':
                self.equals(*instruction[1:])
        return self.registers['z'] == 0, len(self.model_number) - len(digits) - 1
    

def get_next_number(current, index):
    # index = len(current) - 1
    next = [*current]
    while index >= 0:
        print(index)
        next[index] -= 1
        if next[index] == 0:
            next[index] = 9
        else:
            break
        index -= 1
    return next


def part_1(override_inputs = None):
    instructions = get_inputs(parse_input) if override_inputs is None else override_inputs
    logic_unit = LogicUnit(instructions, [9 for _ in range(14)])
    is_valid, digit_to_change = False, 13
    while not is_valid:
        print(logic_unit.model_number)
        logic_unit = LogicUnit(instructions, get_next_number(logic_unit.model_number, digit_to_change))
        is_valid, digit_to_change = logic_unit.check_is_valid()
    return logic_unit.model_number


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
