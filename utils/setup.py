import os


def get_tqdm_kwargs(file: str, part: int, disable=False):
    return {
        'desc': f'{os.path.basename(os.path.dirname(file))} part {part}',
        'disable': disable,
        'leave': False,
    }


def read_inputs(script_directory: str, filename='inputs.txt'):

    with open(f'{script_directory}/{filename}') as file:
        lines = file.readlines()

    return lines
