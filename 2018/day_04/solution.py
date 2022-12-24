import os
import re
import sys
from collections import defaultdict
from datetime import datetime
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    stripped_record = input.strip()
    return [datetime.fromisoformat(stripped_record[1:17]), stripped_record[19:]]


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def get_sleep_counts(records):
    active_guard = None
    sleep_counts = defaultdict(lambda: defaultdict(int))
    sleep_minute = None

    for record in records:
        if '#' in record[1]:
            active_guard = int(re.search(r'\#[0-9]+', record[1]).group(0)[1:])
            sleep_minute = None
        elif record[1] == 'falls asleep':
            sleep_minute = record[0].minute
        else:
            for minute in range(sleep_minute, record[0].minute):
                sleep_counts[active_guard][minute] += 1
            sleep_minute = None

    return sleep_counts


def part_1(override_inputs = None):
    records = get_inputs(parse_input) if override_inputs is None else override_inputs
    sorted_records = sorted(records, key=lambda record: record[0])

    sleep_counts = get_sleep_counts(sorted_records)

    sleepiest_guard = max(sleep_counts.items(), key=lambda sleep_count: sum(sleep_count[1].values()))
    sleepiest_minute = max(sleepiest_guard[1].items(), key=lambda minutes: minutes[1])[0]

    return sleepiest_guard[0] *  sleepiest_minute


def part_2(override_inputs = None):
    records = get_inputs(parse_input) if override_inputs is None else override_inputs
    sorted_records = sorted(records, key=lambda record: record[0])

    sleep_counts = get_sleep_counts(sorted_records)

    sleepiest_guard = max(sleep_counts.items(), key=lambda sleep_count: max(sleep_count[1].values()))
    sleepiest_minute = max(sleepiest_guard[1].items(), key=lambda minutes: minutes[1])[0]

    return sleepiest_guard[0] *  sleepiest_minute


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
