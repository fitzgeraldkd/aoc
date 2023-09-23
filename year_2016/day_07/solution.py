import os
import re


def parse_input(input: str):
    return input.strip()


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def has_abba(string: str):
    if len(string) < 4:
        return False

    for index, first_letter in enumerate(string[:-3]):
        second_letter = string[index+1]
        if first_letter == second_letter:
            continue
        if string[index+2] == second_letter and string[index+3] == first_letter:
            return True
    return False


def split_address(address: str):
    main_sequences = []
    hypernet_sequences = []
    address_parts = re.split(r'(\[|\])', address)
    active_sequences = main_sequences
    for part in address_parts:
        if part == '[':
            active_sequences = hypernet_sequences
        elif part == ']':
            active_sequences = main_sequences
        else:
            active_sequences.append(part)
    return main_sequences, hypernet_sequences


def part_1():
    inputs = get_inputs()
    count = 0
    for input in inputs:
        main_sequences, hypernet_sequences = split_address(input)
        main_sequence_abba = any(has_abba(sequence) for sequence in main_sequences)
        hypernet_sequence_abba = any(has_abba(sequence) for sequence in hypernet_sequences)
        if main_sequence_abba and not hypernet_sequence_abba:
            count += 1
    return count


def part_2():
    inputs = get_inputs()
    count = 0
    for address in inputs:
        main_sequences, hypernet_sequences = split_address(address)
        is_valid = False
        for main_sequence in main_sequences:
            if is_valid:
                break
            if len(main_sequence) < 3:
                continue

            for index, first_letter in enumerate(main_sequence[:-2]):
                second_letter = main_sequence[index+1]
                if first_letter != second_letter and main_sequence[index+2] == first_letter:
                    bab = f'{second_letter}{first_letter}{second_letter}'
                    if any(bab in hypernet_sequence for hypernet_sequence in hypernet_sequences):
                        count += 1
                        is_valid = True
                        break

    return count


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
