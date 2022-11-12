import timeit

import solution as day_01

REPETITIONS = 1000

def benchmark_day_1():
    print(timeit.timeit(day_01.part_1, number=REPETITIONS))
    print(timeit.timeit(day_01.part_2, number=REPETITIONS))


if __name__ == '__main__':
    benchmark_day_1()
