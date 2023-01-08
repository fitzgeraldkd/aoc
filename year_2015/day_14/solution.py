from utils.setup import read_inputs


RACE_DURATION = 2503


def parse_input(input: str):
    name = input.split(' ')[0]
    speed = int(input.split(' ')[3])
    duration = int(input.split(' ')[6])
    rest = int(input.split(' ')[-2])

    return {
        'name': name,
        'speed': speed,
        'duration': duration,
        'rest': rest
    }


def get_inputs():
    return [parse_input(line) for line in read_inputs(__file__)]


def get_distance(reindeer, time):
    cycle_duration = reindeer['duration'] + reindeer['rest']
    cycle_distance = reindeer['speed'] * reindeer['duration']
    full_cycles = time // cycle_duration
    additional_time = time % cycle_duration
    additional_distance = min(additional_time, reindeer['duration']) * reindeer['speed']
    return (cycle_distance * full_cycles) + additional_distance


def is_resting(reindeer, time):
    cycle_duration = reindeer['duration'] + reindeer['rest']
    time_in_cycle = time % cycle_duration
    return time_in_cycle >= reindeer['duration']


def part_1():
    inputs = get_inputs()

    distances = [get_distance(reindeer, RACE_DURATION) for reindeer in inputs]

    return max(distances)


def part_2():
    inputs = get_inputs()

    point_map = {}
    position_map = {}
    for reindeer in inputs:
        point_map[reindeer['name']] = 0
        position_map[reindeer['name']] = 0

    for time in range(RACE_DURATION):
        for reindeer in inputs:
            if not is_resting(reindeer, time):
                position_map[reindeer['name']] += reindeer['speed']

        leading_distance = 0
        leading_reindeer = []
        for reindeer in inputs:
            distance = position_map[reindeer['name']]
            if distance == leading_distance:
                leading_reindeer.append(reindeer['name'])
            elif distance > leading_distance:
                leading_distance = distance
                leading_reindeer = [reindeer['name']]

        for reindeer in leading_reindeer:
            point_map[reindeer] += 1

    return max(point_map.values())


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
