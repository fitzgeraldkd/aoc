import operator
import os
import sys
from typing import Callable

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

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

    def get_ticks_to_move_away(self):
        ticks = []

        for i in range(3):
            p = self.position[i]
            v = self.velocity[i]
            a = self.acceleration[i]
            # d = at^2 + vt + p
            
        return max(ticks)

    def move(self):
        previous_distance = self.get_distance()
        # print('test')
        # print(self.velocity)
        self.velocity = list(map(operator.add, self.velocity, self.acceleration))
        # print(list(self.velocity))
        self.position = list(map(operator.add, self.position, self.velocity))
        if self.get_distance() > previous_distance:
            self.moving_closer = False


def parse_input(input: str, id: int):
    return Particle(input.strip(), id)


def get_inputs(parser: Callable):
    script_directory = os.path.dirname(os.path.realpath(__file__))
    return [parser(line, id) for id, line in enumerate(read_inputs(script_directory))]


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

    while any(particle.moving_closer for particle in particles):
        for particle in particles:
            particle.move()
        # (particle.move() for particle in particles)
        # print(particles[0].get_distance())
        # print(particles[0].position)
        print(len(list(filter(lambda p: p.moving_closer, particles))))
        input()

    return min(particles).id

    return None


def part_2(override_inputs = None):
    particles = get_inputs(parse_input) if override_inputs is None else override_inputs

    return None


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
