import os


def parse_input(input: str):
    split_input = input.strip()[:-1].split('-')
    room_name = ' '.join(split_input[:-1])
    sector_id, checksum = split_input[-1].split('[')
    return room_name, int(sector_id), checksum


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def count_letters(room_name):
    letter_sum = {}
    for letter in room_name:
        if letter == ' ':
            continue
        if letter in letter_sum:
            letter_sum[letter] += 1
        else:
            letter_sum[letter] = 1
    return letter_sum

def get_checksum(room_name):
    counted_letters = count_letters(room_name)
    letters = sorted(sorted(counted_letters.keys()), key=lambda letter: counted_letters[letter], reverse=True)

    return ''.join(letters[:5])


def decrypt_room_name(room_name, sector_id):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = []
    for letter in room_name:
        if letter == ' ':
            decrypted.append(' ')
            continue
        decrypted.append(alphabet[(alphabet.index(letter) + sector_id) % 26])
    return ''.join(decrypted)

def part_1():
    inputs = get_inputs()

    total = 0
    for room_name, sector_id, checksum in inputs:
        if checksum == get_checksum(room_name):
            total += sector_id

    return total


def part_2():
    inputs = get_inputs()

    for room_name, sector_id, checksum in inputs:
        if checksum == get_checksum(room_name):
            if decrypt_room_name(room_name, sector_id) == 'northpole object storage':
                return sector_id

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
