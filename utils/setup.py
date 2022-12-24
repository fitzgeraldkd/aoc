import os


def get_tqdm_kwargs(file: str, part: int, disable=False):
    return {
        'desc': f'{os.path.basename(os.path.dirname(file))} part {part}',
        'disable': disable,
        'leave': False,
    }


def read_inputs(file: str, filename='inputs.txt'):
    script_directory = os.path.dirname(os.path.realpath(file))

    with open(f'{script_directory}/{filename}') as inputs:
        lines = inputs.readlines()

    return lines
