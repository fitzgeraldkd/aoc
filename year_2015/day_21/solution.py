import itertools
import math


WEAPONS = [
    { 'name': 'Dagger', 'cost': 8, 'damage': 4, 'armor': 0 },
    { 'name': 'Shortsword', 'cost': 10, 'damage': 5, 'armor': 0 },
    { 'name': 'Warhammer', 'cost': 25, 'damage': 6, 'armor': 0 },
    { 'name': 'Longsword', 'cost': 40, 'damage': 7, 'armor': 0 },
    { 'name': 'Greataxe', 'cost': 74, 'damage': 8, 'armor': 0 }
]

ARMOR = [
    { 'name': 'Leather', 'cost': 13, 'damage': 0, 'armor': 1 },
    { 'name': 'Chainmail', 'cost': 31, 'damage': 0, 'armor': 2 },
    { 'name': 'Splitmail', 'cost': 53, 'damage': 0, 'armor': 3 },
    { 'name': 'Bandedmail', 'cost': 75, 'damage': 0, 'armor': 4 },
    { 'name': 'Platemail', 'cost': 102, 'damage': 0, 'armor': 5 }
]

RINGS = [
    { 'name': 'Damage +1', 'cost': 25, 'damage': 1, 'armor': 0 },
    { 'name': 'Damage +2', 'cost': 50, 'damage': 2, 'armor': 0 },
    { 'name': 'Damage +3', 'cost': 100, 'damage': 3, 'armor': 0 },
    { 'name': 'Defense +1', 'cost': 20, 'damage': 0, 'armor': 1 },
    { 'name': 'Defense +2', 'cost': 40, 'damage': 0, 'armor': 2 },
    { 'name': 'Defense +3', 'cost': 80, 'damage': 0, 'armor': 3 },
]


def get_inputs():
    return {
        'hp': 109,
        'damage': 8,
        'armor': 2
    }


def get_stats(equipment):
    damage = 0
    armor = 0
    cost = 0

    for item in equipment:
        damage += item['damage']
        armor += item['armor']
        cost += item['cost']

    return ({
        'hp': 100,
        'damage': damage,
        'armor': armor
    }, cost)


def fight(player, boss):
    player_damage = player['damage'] - boss['armor']
    boss_damage = boss['damage'] - player['armor']

    player_turns_to_win = math.ceil(boss['hp'] / player_damage) if player_damage > 0 else math.inf
    boss_turns_to_win = math.ceil(player['hp'] / boss_damage) if boss_damage > 0 else math.inf

    winner = 'player' if player_turns_to_win <= boss_turns_to_win else 'boss'

    return (winner, min(player_turns_to_win, boss_turns_to_win))


def part_1():
    boss = get_inputs()

    winning_costs = []

    def run_simulation(equipment):
        player, cost = get_stats(equipment)

        winner, _ = fight(player, boss)
        if winner == 'player':
            winning_costs.append(cost)

    ring_sets = []
    ring_sets.extend([ring] for ring in RINGS)
    ring_sets.extend(itertools.permutations(RINGS, 2))

    for weapon in WEAPONS:
        run_simulation([weapon])

        for ring_set in ring_sets:
            equipment = [weapon]
            equipment.extend(ring_set)
            run_simulation(equipment)

        for armor in ARMOR:
            run_simulation([weapon, armor])

            for ring_set in ring_sets:
                equipment = [weapon, armor]
                equipment.extend(ring_set)
                run_simulation(equipment)

    return min(winning_costs)


def part_2():
    boss = get_inputs()

    winning_costs = []

    def run_simulation(equipment):
        player, cost = get_stats(equipment)

        winner, _ = fight(player, boss)
        if winner == 'boss':
            winning_costs.append(cost)

    ring_sets = []
    ring_sets.extend([ring] for ring in RINGS)
    ring_sets.extend(itertools.permutations(RINGS, 2))

    for weapon in WEAPONS:
        run_simulation([weapon])

        for ring_set in ring_sets:
            equipment = [weapon]
            equipment.extend(ring_set)
            run_simulation(equipment)

        for armor in ARMOR:
            run_simulation([weapon, armor])

            for ring_set in ring_sets:
                equipment = [weapon, armor]
                equipment.extend(ring_set)
                run_simulation(equipment)

    return max(winning_costs)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
