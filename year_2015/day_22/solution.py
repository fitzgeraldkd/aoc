import copy
import json

from classes.PriorityQueue import PriorityQueue


PLAYER = { 'hp': 50, 'mp': 500 }
BOSS = { 'hp': 51, 'damage': 9 }

SPELLS = [
    { 'name': 'Magic Missile', 'cost': 53, 'damage': 4, 'heal': 0, 'effect': None },
    { 'name': 'Drain', 'cost': 73, 'damage': 2, 'heal': 2, 'effect': None },
    { 'name': 'Shield', 'cost': 113, 'damage': 0, 'heal': 0, 'effect': 'shield' },
    { 'name': 'Poison', 'cost': 173, 'damage': 0, 'heal': 0, 'effect': 'poison' },
    { 'name': 'Recharge', 'cost': 229, 'damage': 0, 'heal': 0, 'effect': 'recharge' }
]

EFFECTS = {
    'shield': 6,
    'poison': 6,
    'recharge': 5
}


def get_inputs():
    return BOSS


def run_effects(game_state):
    effects = game_state['effects']

    armor = 0
    if 'shield' in effects:
        effects['shield'] -= 1
        armor = 7
        if effects['shield'] == 0:
            del effects['shield']

    if 'recharge' in effects:
        game_state['player']['mp'] += 101
        effects['recharge'] -= 1
        if effects['recharge'] == 0:
            del effects['recharge']

    if 'poison' in effects:
        game_state['boss']['hp'] -= 3
        effects['poison'] -= 1
        if effects['poison'] == 0:
            del effects['poison']

    return armor


def new_turn(old_game_state, spell, queue, checked_states, hard_mode = False):
    game_state = copy.deepcopy(old_game_state)
    checked_states.add(json.dumps(game_state))

    if hard_mode:
        game_state['player']['hp'] -= 1
        if game_state['player']['hp'] <= 0:
            return None


    armor = run_effects(game_state)
    if game_state['boss']['hp'] <= 0:
        return game_state

    # Player's turn.
    game_state['player']['mp'] -= spell['cost']
    game_state['player']['hp'] += spell['heal']
    game_state['boss']['hp'] -= spell['damage']
    game_state['mana_spent'] += spell['cost']
    if spell['effect']:
        game_state['effects'][spell['effect']] = EFFECTS[spell['effect']]

    if game_state['player']['mp'] < 0:
        return None

    if game_state['boss']['hp'] <= 0:
        return game_state

    armor = run_effects(game_state)
    if game_state['boss']['hp'] <= 0:
        return game_state

    # Boss's turn.
    game_state['player']['hp'] -= (game_state['boss']['damage'] - armor)

    if game_state['player']['hp'] <= 0:
        return None

    for next_spell in SPELLS:
        is_effect_active = (next_spell['effect'] is not None and
                            next_spell['effect'] in game_state['effects'] and
                            game_state['effects'][next_spell['effect']] > 1)
        if is_effect_active:
            continue

        if json.dumps(game_state) not in checked_states:
            queue.add_item({'game_state': game_state, 'spell': next_spell}, game_state['mana_spent'] + next_spell['cost'])



def part_1():
    boss = get_inputs()
    player = PLAYER
    game_state = {
        'player': player,
        'boss': boss,
        'is_players_turn': True,
        'effects': {},
        'mana_spent': 0
    }
    queue = PriorityQueue()
    checked_states = set()

    for spell in SPELLS:
        queue.add_item({'game_state': game_state, 'spell': spell}, game_state['mana_spent'] + spell['cost'])

    while not queue.is_empty():
        item = queue.pop()
        winning_game_state = new_turn(item['game_state'], item['spell'], queue, checked_states)
        if winning_game_state:
            return winning_game_state['mana_spent']

    return None


def part_2():
    boss = get_inputs()
    player = PLAYER
    game_state = {
        'player': player,
        'boss': boss,
        'is_players_turn': True,
        'effects': {},
        'mana_spent': 0
    }
    queue = PriorityQueue()
    checked_states = set()

    for spell in SPELLS:
        queue.add_item({'game_state': game_state, 'spell': spell}, game_state['mana_spent'] + spell['cost'])

    while not queue.is_empty():
        item = queue.pop()
        winning_game_state = new_turn(item['game_state'], item['spell'], queue, checked_states, hard_mode=True)
        if winning_game_state:
            return winning_game_state['mana_spent']

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
