from collections import defaultdict
import operator
from typing import Callable

from utils.setup import read_inputs


class Particle:
    def __init__(self, particle_string, id):
        raw_position, raw_velocity, raw_acceleration = particle_string.split(', ')
        self.position = [int(value) for value in raw_position[3:-1].split(',')]
        self.velocity = [int(value) for value in raw_velocity[3:-1].split(',')]
        self.acceleration = [int(value) for value in raw_acceleration[3:-1].split(',')]
        self.moving_closer = True
        self.id = id

    def __iter__(self):
        return self.get_distance

    def get_distance(self):
        return sum(self.position)

    def move(self):
        previous_distance = self.get_distance()
        self.velocity = list(map(operator.add, self.velocity, self.acceleration))
        self.position = list(map(operator.add, self.position, self.velocity))
        if self.get_distance() > previous_distance:
            self.moving_closer = False


def parse_input(input: str, id: int):
    return Particle(input.strip(), id)


def get_inputs(parser: Callable):
    return [parser(line, id) for id, line in enumerate(read_inputs(__file__))]


def part_1(override_inputs = None):
    particles = get_inputs(parse_input) if override_inputs is None else override_inputs

    closest_particle = None
    closest_particle_acceleration = None
    for particle in particles:
        particle_acceleration = sum(abs(a) for a in particle.acceleration)
        if closest_particle is None or particle_acceleration < closest_particle_acceleration:
            closest_particle = particle
            closest_particle_acceleration = particle_acceleration
        elif particle_acceleration == closest_particle_acceleration:
            particle_velocity = sum(abs(v) for v in particle.velocity)
            closest_particle_velocity = sum(abs(v) for v in closest_particle.velocity)
            if particle_velocity < closest_particle_velocity:
                closest_particle = particle
            elif particle_velocity == closest_particle_velocity and particle.get_distance() < closest_particle.get_distance():
                closest_particle = particle


    return closest_particle.id


def part_2(override_inputs = None):
    particles = get_inputs(parse_input) if override_inputs is None else override_inputs

    for _ in range(1000):
        location_map = defaultdict(list)
        for particle in particles:
            particle.move()
            location_map[''.join(str(coord) for coord in particle.position)].append(particle)
        for location in location_map:
            if len(location_map[location]) > 1:
                for particle in location_map[location]:
                    particles.remove(particle)

    return len(particles)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
