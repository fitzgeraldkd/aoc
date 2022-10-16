def get_inputs():
    return 3083, 2978

def get_index(x, y):
    index = 1
    for i in range(x-1):
        index += i + 2
    
    for i in range(y-1):
        index += x + i
    
    return index


def part_1():
    x, y = get_inputs()
    print(get_index(x, y))

    code = 20151125

    for _ in range(get_index(x, y) - 1):
        code = (code * 252533) % 33554393

    return code


def part_2():
    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
