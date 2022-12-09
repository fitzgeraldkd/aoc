import os
import sys
from collections import defaultdict
from typing import Callable, Dict, List, Tuple

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip().split()[-1])


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    positions = get_inputs(parse_input) if override_inputs is None else override_inputs
    scores = [0, 0]
    target_score = 1000
    rolls = 0
    current_player = 0
    current_roll = 1

    while max(scores) < target_score:
        for _ in range(3):
            positions[current_player] = (positions[current_player] + current_roll - 1) % 10 + 1
            current_roll = (current_roll % 100) + 1
            rolls += 1
        scores[current_player] += positions[current_player]

        current_player = 1 if current_player == 0 else 0

    return min(scores) * rolls


def part_2(override_inputs = None):
    player_1, player_2 = get_inputs(parse_input) if override_inputs is None else override_inputs

    target_score = 21

    player_state: Dict[Tuple[Tuple[int, int], Tuple[int, int]], int] = defaultdict(int)
    player_state[((player_1, 0), (player_2, 0))] = 1
    player_wins = [0, 0]

    # Determine the possible rolls, along with the number of universes they will occur in.
    ROLLS = defaultdict(int)
    for i in range(1, 4):
        for j in range(1, 4):
            for k in range(1, 4):
                ROLLS[i + j + k] += 1

    # Run the game until there are no incomplete states left.
    while sum(player_state.values()) != 0:

        # Each player takes a turn in each round.
        for player in range(2):
            other_player = 0 if player == 1 else 1
            new_state: Dict[Tuple[Tuple[int, int], Tuple[int, int]], int] = defaultdict(int)

            # Each group of incomplete universes progress.
            for key, universes in player_state.items():
                position, points = key[player]
                other_player_key = key[other_player]

                # Create the new universes for each roll.
                for distance, rolls in ROLLS.items():
                    new_position = (position + distance - 1) % 10 + 1
                    new_score = points + new_position
                    if new_score < target_score:
                        current_player_key = (new_position, new_score)
                        new_key = ((current_player_key, other_player_key) if player == 0 else
                                   (other_player_key, current_player_key))
                        new_state[new_key] += universes * rolls
                    else:
                        player_wins[player] += universes * rolls
            player_state = new_state

    return max(player_wins)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
