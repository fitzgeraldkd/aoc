def read_inputs(script_directory: str, filename='inputs.txt'):

    with open(f'{script_directory}/{filename}') as file:
        lines = file.readlines()

    return lines
