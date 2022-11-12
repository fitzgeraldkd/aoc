import timeit
import os
import sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))


import solution as day_01
from utils.constants import BENCHMARK_REPTITIONS


def benchmark_day_1():
    print(timeit.timeit(day_01.part_1, number=BENCHMARK_REPTITIONS))
    print(timeit.timeit(day_01.part_2, number=BENCHMARK_REPTITIONS))


if __name__ == '__main__':
    benchmark_day_1()
