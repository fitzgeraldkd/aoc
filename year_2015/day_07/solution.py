from utils.setup import read_inputs


TARGET_WIRE = 'a'


def parse_input(input: str):
    split_input = input.strip().split(' -> ')

    action = None

    for action_to_split in ['AND', 'LSHIFT', 'OR', 'RSHIFT']:
        if action_to_split in split_input[0]:
            action = action_to_split
            values = split_input[0].split(f' {action} ')

    if 'NOT' in split_input[0]:
        action = 'NOT'
        values = [split_input[0][4:]]

    if action is None:
        action = 'ASSIGN'
        values = [split_input[0]]

    return {
        'action': action,
        'destination': split_input[1],
        'values': values
    }


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def get_value(wires, label, calculated_wires):

    if label in calculated_wires:
        return calculated_wires[label]

    wire = wires[label]

    def read_input(wires, input):
        try:
            return int(input)
        except ValueError:
            return get_value(wires, input, calculated_wires)

    inputs = [read_input(wires, input) for input in wire['inputs']]

    if wire['action'] == 'AND':
        value = inputs[0] & inputs[1]
    elif wire['action'] == 'ASSIGN':
        value = inputs[0]
    elif wire['action'] == 'LSHIFT':
        value = inputs[0] << inputs[1]
    elif wire['action'] == 'NOT':
        value = ~inputs[0]
    elif wire['action'] == 'OR':
        value = inputs[0] | inputs[1]
    elif wire['action'] == 'RSHIFT':
        value = inputs[0] >> inputs[1]

    while value > 65535:
        value -= 65536

    while value < 0:
        value += 65536

    calculated_wires[label] = value
    return value


def part_1():
    inputs = get_inputs()

    wires = {}

    for input in inputs:
        wires[input['destination']] = {
            'action': input['action'],
            'inputs': input['values']
        }

    return get_value(wires, TARGET_WIRE, {})


def part_2():
    inputs = get_inputs()

    wires = {}

    for input in inputs:
        wires[input['destination']] = {
            'action': input['action'],
            'inputs': input['values']
        }

    wires['b'] = {
        'action': 'ASSIGN',
        'inputs': [part_1()]
    }

    return get_value(wires, TARGET_WIRE, {})


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
