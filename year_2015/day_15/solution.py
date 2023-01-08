from functools import reduce

from utils.setup import read_inputs


def parse_input(input: str):
    [name, properties] = input.strip().split(': ')
    properties = properties.split(', ')
    ingredient = {
        'capacity': int(properties[0].split(' ')[1]),
        'durability': int(properties[1].split(' ')[1]),
        'flavor': int(properties[2].split(' ')[1]),
        'texture': int(properties[3].split(' ')[1]),
        'calories': int(properties[4].split(' ')[1])
    }
    return (name, ingredient)


def get_inputs():
    return { ingredient[0]: ingredient[1] for ingredient in [parse_input(line) for line in read_inputs(__file__)]}


def calculate_score(ingredients, amounts):
    totals = {
        'capacity': 0,
        'durability': 0,
        'flavor': 0,
        'texture': 0
    }

    for ingredient in ingredients.keys():
        for property in ['capacity', 'durability', 'flavor', 'texture']:
            totals[property] += ingredients[ingredient][property] * amounts[ingredient]

    return reduce(lambda x, y: x * y, [max(value, 0) for value in totals.values()])


def optimize_ingredient(ingredients, ingredient, amounts):
    previous_score = calculate_score(ingredients, amounts)

    for ingredient_to_remove in filter(lambda name: name != ingredient, ingredients.keys()):

        while calculate_score(ingredients, amounts) >= previous_score and amounts[ingredient_to_remove] > 1:
            previous_score = calculate_score(ingredients, amounts)
            amounts[ingredient] += 1
            amounts[ingredient_to_remove] -= 1

        amounts[ingredient] -= 1
        amounts[ingredient_to_remove] += 1

    return amounts


def get_calories(ingredients, amounts):
    return sum([ingredients[ingredient]['calories'] * amounts[ingredient] for ingredient in ingredients.keys()])


def part_1():
    ingredients = get_inputs()
    ingredient_names = list(ingredients.keys())
    amounts = {}

    for ingredient in ingredient_names[:-1]:
        amounts[ingredient] = 100 // len(ingredients)
    amounts[ingredient_names[-1]] = 100 - sum(amounts.values())

    previous_score = 0

    while calculate_score(ingredients, amounts) > previous_score:
        previous_score = calculate_score(ingredients, amounts)
        for ingredient in ingredients.keys():
            amounts = optimize_ingredient(ingredients, ingredient, amounts)

    return calculate_score(ingredients, amounts)


def part_2():
    ingredients = get_inputs()
    amounts = {}

    best_score = 0

    ingredient_names = list(ingredients.keys())

    # Assumes 4 ingredients.
    for i in range(97):
        x = i + 1
        amounts[ingredient_names[0]] = x
        for j in range(97 - x):
            y = j + 1
            amounts[ingredient_names[1]] = y
            for k in range(97 - x - y):
                z = k + 1
                amounts[ingredient_names[2]] = z
                amounts[ingredient_names[3]] = 100 - x - y - z
                if get_calories(ingredients, amounts) == 500:
                    best_score = max(best_score, calculate_score(ingredients, amounts))



    return best_score


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
