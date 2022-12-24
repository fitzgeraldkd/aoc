import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs

REVERSE_OPERATOR_MAP = {
    '+': '-',
    '-': '+',
    '*': '/',
    '/': '*',
    '==': '=='
}


def parse_input(input: str):
    param, *args = input.strip().split(' ')
    if len(args) == 1:
        value = args[0]
        arg_1, operator, arg_2 = None, None, None
    else:
        value = None
        arg_1, operator, arg_2 = args
    return {
        'param': param[:-1],
        'arg_1': arg_1,
        'arg_2': arg_2,
        'operator': operator,
        'value': value
    }
    return input.strip()
    return int(input.strip())


def get_inputs(parser: Callable):
    # return [parser(line) for line in read_inputs(__file__)]
    return [parser(line) for line in read_inputs(__file__, 'sample.txt')]


def get_value(instructions, key):
    instruction = instructions[key]
    if instruction['value'] is None:
        arg_1 = get_value(instructions, instruction['arg_1'])
        arg_2 = get_value(instructions, instruction['arg_2'])
        value = eval(f'{arg_1}{instruction["operator"]}{arg_2}')
        instruction['value'] = value
        return value
    else:
        return instruction['value']

def get_reverse_value(instructions, reverse_instructions, key):
    instruction = reverse_instructions[key]
    if instruction['value'] is None:
        print(instruction)
        if is_dependent(instructions, instruction['arg_1'], key) and instruction['arg_1'] != 'root':
            value_1 = get_reverse_value(instructions, reverse_instructions, instruction['arg_1'])
        else:
            value_1 = get_value(instructions, instruction['arg_1'])

        if is_dependent(instructions, instruction['arg_2'], key) and instruction['arg_2'] != 'root':
            value_2 = get_reverse_value(instructions, reverse_instructions, instruction['arg_2'])
        else:
            value_2 = get_value(instructions, instruction['arg_2'])
        # value_1 = get_value(reverse_instructions if is_dependent(reverse_instructions, instruction['arg_1'], 'root') else instructions, instruction['arg_1'])
        # value_2 = get_value(reverse_instructions if is_dependent(reverse_instructions, instruction['arg_2'], 'root') else instructions, instruction['arg_2'])
        value = eval(f'{value_1} {instruction["operator"]} {value_2}')
        print(value)
        instruction['value'] = value
        return value
    else:
        return instruction['value']


def reverse_value(instructions, key, variable_key, parent_key, sibling_key):
    # if key == variable_key:
    #     return get_value(instructions, parent_key)

    instruction = instructions[key]
    args = [instruction['arg_1'], instruction['arg_2']]
    operator = REVERSE_OPERATOR_MAP[instructions[parent_key]['operator']]
    first_arg_dependent = is_dependent(instructions, args[0], variable_key)
    dependent_arg = args[0] if first_arg_dependent else args[1]
    independent_arg = args[1] if first_arg_dependent else args[0]

    if operator == '==':
        instruction['value'] = instructions[parent_key]['value']
    else:
        first_key = parent_key if first_arg_dependent else independent_arg
        second_key = independent_arg if first_arg_dependent else parent_key
        instruction['value'] = eval(f'{get_value(instructions, first_key)} {operator} {get_value(instructions, second_key)}')
        print(instruction, instruction['value'])

    if key == variable_key:
        return instruction['value']

    print(instructions)
    return reverse_value(instructions, key=dependent_arg, variable_key=variable_key, parent_key=key, sibling_key=independent_arg)

    if key == variable_key:
        return get_value(instructions, parent_key)

    instruction = instructions[key]
    args = [instruction['arg_1'], instruction['arg_2']]
    operator = REVERSE_OPERATOR_MAP[instructions[parent_key]['operator']]
    first_arg_dependent = is_dependent(instructions, args[0], variable_key)
    dependent_arg = args[0] if first_arg_dependent else args[1]
    independent_arg = args[1] if first_arg_dependent else args[0]
    if operator == '==' or parent_key == 'vglr':
        instruction['value'] = instructions[parent_key]['value']
    else:
        first_key = parent_key if first_arg_dependent else independent_arg
        second_key = independent_arg if first_arg_dependent else parent_key
        instruction['value'] = eval(f'{get_value(instructions, first_key)} {operator} {get_value(instructions, second_key)}')

        print()
        print(f'{instruction["arg_1"]} {instruction["operator"]} {instruction["arg_2"]}', instruction)
        print(instructions[first_key]['value'], instructions[second_key]['value'], instruction['value'])

    return reverse_value(instructions, key=dependent_arg, variable_key=variable_key, parent_key=key)
    # # print(instruction)
    # args = [instruction['arg_1'], instruction['arg_2']]
    # if is_dependent(instructions, args[0], variable_key):
    #     dependent_arg = args[0]
    #     independent_arg = args[1]
    # else:
    #     dependent_arg = args[1]
    #     independent_arg = args[0]
    # # independent_value = get_value(instructions, independent_arg)
    # instruction['value'] = eval(f'{get_value(instructions, parent_key)} {REVERSE_OPERATOR_MAP[instruction["operator"]]} {get_value(instructions, independent_arg)}')
    # print(instruction)
    # return reverse_value(instructions, key=dependent_arg, variable_key=variable_key, parent_key=key)



def is_dependent(instructions, instruction_key, dependent_key):
    # print(instructions, instruction_key, dependent_key)
    if instruction_key == dependent_key:
        return True
    if instruction_key is None:
        return False
    instruction = instructions[instruction_key]
    if instruction['arg_1'] is None and instruction['arg_2'] is None:
        return False
    if dependent_key in [instruction['arg_1'], instruction['arg_2']]:
        return True
    return is_dependent(instructions, instruction['arg_1'], dependent_key) or is_dependent(instructions, instruction['arg_2'], dependent_key)


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    mapped_instructions = { instruction['param']: instruction for instruction in inputs }
    return get_value(mapped_instructions, 'root')


def part_2(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs
    mapped_instructions = { instruction['param']: instruction for instruction in inputs }
    variable_key = 'humn'
    # mapped_instructions[variable_key]['value'] = 3342154812537
    # 3342154812537
    # 8764479278274.196
    # print(get_value(mapped_instructions, 'qhbp'))
    # print(get_value(mapped_instructions, 'vglr'))
    # mapped_instructions['vglr']['value'] *= 2
    # print(get_value(mapped_instructions, 'jmws'))
    mapped_instructions['root']['operator'] = '=='
    # print(get_value(mapped_instructions, 'qhbp') > get_value(mapped_instructions, 'vglr'))
    reverse_instructions = {}

    for param in mapped_instructions:
        reverse_instructions[param] = {
            'param': param,
            'value': None if param == variable_key else mapped_instructions[param]['value'],
            'arg_1': None,
            'arg_2': None,
            'operator': None
        }


    for param in mapped_instructions:
        args = [mapped_instructions[param][arg] for arg in ['arg_1', 'arg_2']]
        if all(args):
            reverse_instructions[args[0]]['arg_1'] = param
            reverse_instructions[args[0]]['arg_2'] = args[1]
            reverse_instructions[args[0]]['operator'] = REVERSE_OPERATOR_MAP[mapped_instructions[param]['operator']]
            reverse_instructions[args[1]]['arg_1'] = param
            reverse_instructions[args[1]]['arg_2'] = args[0]
            reverse_instructions[args[1]]['operator'] = REVERSE_OPERATOR_MAP[mapped_instructions[param]['operator']]



    output =  get_reverse_value(mapped_instructions, reverse_instructions, variable_key)
    for key in reverse_instructions:
        print(reverse_instructions[key] if reverse_instructions[key]['value'] is not None else mapped_instructions[key])
    # for value in reverse_instructions.values():
    #     print(value)
    # for value in mapped_instructions.values():
    #     print(value)
    return output

    root_args = [mapped_instructions['root']['arg_1'], mapped_instructions['root']['arg_2']]
    if is_dependent(mapped_instructions, root_args[0], variable_key):
        dependent_arg = root_args[0]
        independent_arg = root_args[1]
    else:
        dependent_arg = root_args[1]
        independent_arg = root_args[0]
    mapped_instructions['root']['value'] = get_value(mapped_instructions, independent_arg)
    return reverse_value(mapped_instructions, dependent_arg, variable_key, independent_arg)

    independent_value = get_value(mapped_instructions, independent_arg)
    mapped_instructions['root']['value'] = independent_value




if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
