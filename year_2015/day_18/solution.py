import os


def parse_input(input: str):
    return [item == '#' for item in list(input.strip())]


def get_inputs():
    script_dir = os.path.dirname(os.path.realpath(__file__))
    file = open(f'{script_dir}/inputs.txt')
    inputs = [parse_input(line) for line in file.readlines()]
    file.close()
    return inputs


def count_neighbors(grid):
    neighbors = []
    for y, row in enumerate(grid):
        neighbors.append([])
        for x, cell in enumerate(row):
            delta_x = [0]
            delta_y = [0]

            if y == 0:
                delta_y.append(1)
            elif y == len(grid) - 1:
                delta_y.append(-1)
            else:
                delta_y.extend([1, -1])

            if x == 0:
                delta_x.append(1)
            elif x == len(row) - 1:
                delta_x.append(-1)
            else:
                delta_x.extend([1, -1])

            count = 0
            for dx in delta_x:
                for dy in delta_y:
                    if dx == 0 and dy == 0:
                        continue
                    count += grid[y+dy][x+dx]

            neighbors[y].append(count)

    return neighbors


def count_lights(grid):
    count = 0

    for row in grid:
        count += len(list(filter(None, row)))
    
    return count


def part_1():
    grid = get_inputs()

    for _ in range(100):
        neighbors = count_neighbors(grid)
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                grid[y][x] = (neighbors[y][x] in [2, 3]) if grid[y][x] else (neighbors[y][x] == 3)

    return count_lights(grid)


def part_2():
    grid = get_inputs()

    grid[0][0] = True
    grid[0][len(grid[0]) - 1] = True
    grid[len(grid) - 1][0] = True
    grid[len(grid) - 1][len(grid[0]) - 1] = True

    for _ in range(100):
        neighbors = count_neighbors(grid)
        for y, row in enumerate(grid):
            for x, _ in enumerate(row):
                if x in [0, len(grid[0]) - 1] and y in [0, len(grid) - 1]:
                    continue
                grid[y][x] = (neighbors[y][x] in [2, 3]) if grid[y][x] else (neighbors[y][x] == 3)

    return count_lights(grid)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
