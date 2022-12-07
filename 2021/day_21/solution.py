import os
import sys
from collections import defaultdict
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    return int(input.strip().split()[-1])


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line) for line in read_inputs(script_directory)]


def part_1(override_inputs = None):
    inputs = get_inputs(parse_input) if override_inputs is None else override_inputs

    return None


def part_2(override_inputs = None):
    player_1, player_2 = get_inputs(parse_input) if override_inputs is None else override_inputs

    target_score = 21

    def get_win_states(current_position, current_score, moves, win_states, player):
        moves += 1
        for roll in range(1, 4):
            new_position = (current_position + roll) % 10
            new_score = current_score + new_position
            if new_score >= target_score:
                win_states[moves][0] += 1
                # win_states[moves] += 3 ** ((moves - (1 if player == 1 else 0)) * 2)
            else:
                win_states[moves][1] += 1
                get_win_states(new_position, new_score, moves, win_states, player)
        return win_states


    player_1_win_states = get_win_states(player_1, current_score=0, moves=0, win_states=defaultdict(lambda: [0, 0]), player=1)
    player_2_win_states = get_win_states(player_2, current_score=0, moves=0, win_states=defaultdict(lambda: [0, 0]), player=2)
    print(player_1_win_states)
    print(player_2_win_states)

    for i in range(1, 10):
        if i != 1:
            player_1_win_states[i][0] *= player_2_win_states[i - 1][1]
            player_1_win_states[i][1] *= player_2_win_states[i - 1][1]
        player_2_win_states[i][0] *= player_1_win_states[i][1]
        player_2_win_states[i][1] *= player_1_win_states[i][1]

    print(player_1_win_states)
    print(player_2_win_states)
    print(444356092776315)
    print(341960390180808)
    print(sum(results[0] for results in player_1_win_states.values()))
    print(sum(results[0] for results in player_2_win_states.values()))

    # print(sum([win_1 * win_2 for win_1 in player_1_win_states.values() for win_2 in player_2_win_states.values()]))
    # print(sum([win_1 * win_2 for win_1 in player_1_win_states.values() for win_2 in player_2_win_states.values()]) / (10 ** 14))

    # player_1_adjusted_win_states = defaultdict(int)
    # player_2_adjusted_win_states = defaultdict(int)
    # for i in range(3, 10):
    #     # player_1_adjusted_win_states[i] = player_1_win_states[i] - player_2_win
    #     player_1_win_states[i] = max(player_1_win_states[i] - player_2_win_states[i - 1] * 3, 0)
    #     player_2_win_states[i] = max(player_2_win_states[i] - player_1_win_states[i] * 3, 0)

    # print(player_1_win_states)
    # print(player_2_win_states)
    # print(sum([win_1 * win_2 for win_1 in player_1_win_states.values() for win_2 in player_2_win_states.values()]))
    # print(sum([win_1 * win_2 for win_1 in player_1_win_states.values() for win_2 in player_2_win_states.values()]) / (10 ** 14))


    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
