def read_inputs(script_directory: str):

    with open(f'{script_directory}/inputs.txt') as file:
        lines = file.readlines()

    return lines
