import operator
import os
import sys
from functools import reduce
from typing import Callable, List, Tuple

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.path.pardir, os.path.pardir))

from utils.setup import read_inputs


def parse_input(input: str):
    cmd, coordinates = input.strip().split()
    coordinates = [[int(value) for value in coordinate[2:].split('..')] for coordinate in coordinates.split(',')]
    for coordinate in coordinates:
        if coordinate[0] == coordinate[1]:
            print('EQUAL')
    return (cmd, coordinates)


def get_inputs(parser: Callable):
    return [parser(line) for line in read_inputs(__file__)]


def get_verteces(cluster: List[List[int]]):
    return [(x, y, z) for x in cluster[0] for y in cluster[1] for z in cluster[2]]


def offset_vertex(cluster: List[List[int]], vertex: Tuple[int, int, int]):
    offset = tuple((0 if vertex[i] == cluster[i][0] else 1) for i in range(3))
    return tuple(map(operator.add, vertex, offset))


def is_point_in_cluster(cluster: List[List[int]], point: Tuple[int, int, int]):
    return all(point[i] >= cluster[i][0] and point[i] <= cluster[i][1] for i in range(3))


def split_cluster_at_verteces(cluster: List[List[int]], verteces: List[Tuple[int, int, int]]):
    clusters = [cluster]
    for x, y, z in verteces:
        checked_clusters = []
        while clusters:
            cluster = clusters.pop()
            if is_point_in_cluster(cluster, (x, y, z)):
                checked_clusters.extend([
                    [[cluster[0][0], x - 1], [cluster[1][0], y - 1], [cluster[2][0], z - 1]],
                    [[x, cluster[0][1]], [cluster[1][0], y - 1], [cluster[2][0], z - 1]],
                    [[cluster[0][0], x - 1], [y, cluster[1][1]], [cluster[2][0], z - 1]],
                    [[x, cluster[0][1]], [y, cluster[1][1]], [cluster[2][0], z - 1]],
                    [[cluster[0][0], x - 1], [cluster[1][0], y - 1], [z, cluster[2][1]]],
                    [[x, cluster[0][1]], [cluster[1][0], y - 1], [z, cluster[2][1]]],
                    [[cluster[0][0], x - 1], [y, cluster[1][1]], [z, cluster[2][1]]],
                    [[x, cluster[0][1]], [y, cluster[1][1]], [z, cluster[2][1]]]
                ])
            else:
                checked_clusters.append(cluster)
        clusters = checked_clusters
    return clusters


def subtract_clusters(cluster_a: List[List[int]], cluster_b: List[List[int]]):
    """
    Determine the type of intersection based on the number of verteces from cluster_b are inside of cluster_a.
    Types of intersections:
      - None (0 intersecting verteces) - No intersection.
      - Contain (0 intersecting verteces) - cluster_a is completely inside cluster_b.
      - Extrude (0 intersecting verteces) - A cutaway all the way through cluster_a.
      - Corner (1 intersecting vertex)
      - Notch (2 intersecting verteces)
      - Push (4 intersecting verteces) - Similar to extrude, but not all the way through.
      - Hollow (8 intersecting verteces) - cluster_b is completely inside cluster_a.
    """
    cluster_a_verteces = get_verteces(cluster_a)
    cluster_b_verteces = get_verteces(cluster_b)
    clusters = []
    intersecting_verteces = list(filter(lambda vertex: is_point_in_cluster(cluster_a, vertex), cluster_b_verteces))
    if len(intersecting_verteces) == 0:
        if any([cluster_a[i][0] > cluster_b[i][1] or cluster_a[i][1] < cluster_b[i][0] for i in range(3)]):
            # None.
            clusters.append(cluster_a)
        elif all([is_point_in_cluster(cluster_b, vertex) for vertex in cluster_a_verteces]):
            # Contain.
            # cluster_a is completely contained in cluster_b, no subdividing is necessary.
            pass
        else:
            # Extrude.
            extrusion_axis = [cluster_b[i][0] >= cluster_a[i][0] and cluster_b[i][1] <= cluster_a[i][1] for i in range(3)].index(False)
            print('cluster_a')
            print(cluster_a)
            coordinate_bounds = [[*bound] for bound in cluster_a]
            for axis in range(3):
                # if axis != extrusion_axis:
                    coordinate_bounds[axis] = [max(coordinate_bounds[axis][0], cluster_b[axis][0]),
                                               min(coordinate_bounds[axis][1], cluster_b[axis][1])]
                    boundary_overrides = [
                        [cluster_a[axis][0], coordinate_bounds[axis][0] - 1],
                        [coordinate_bounds[axis][1] + 1, cluster_a[axis][1]]
                    ]
                    print('boundary_overrides', boundary_overrides)
                    print('coordinate_bounds', coordinate_bounds)
                    print('cluster_a', cluster_a)
                    for boundary_override in boundary_overrides:
                        if boundary_override[0] <= boundary_override[1]:
                            new_subcluster = [[*bound] for bound in coordinate_bounds]
                            new_subcluster[axis] = [*boundary_override]
                            clusters.append(new_subcluster)

    elif len(intersecting_verteces) == 1:
        # Corner.
        intersecting_vertex = offset_vertex(cluster_b, intersecting_verteces[0])

    elif len(intersecting_verteces) == 2:
        # Notch.
        pass
    elif len(intersecting_verteces) == 4:
        # Push.
        pass
    elif len(intersecting_verteces) == 8:
        # Hollow.
        clusters.extend([
            [[cluster_a[0][0], cluster_a[0][1]],
             [cluster_a[1][0], cluster_a[1][1]],
             [cluster_a[2][0], cluster_b[2][0] - 1]],
            [[cluster_a[0][0], cluster_a[0][1]],
             [cluster_a[1][0], cluster_a[1][1]],
             [cluster_b[2][1] + 1, cluster_a[2][1]]],

            [[cluster_a[0][0], cluster_a[0][1]],
             [cluster_a[1][0], cluster_b[1][0] - 1],
             [cluster_b[2][0], cluster_b[2][1]]],
            [[cluster_a[0][0], cluster_a[0][1]],
             [cluster_b[1][1] + 1, cluster_a[1][1]],
             [cluster_b[2][0], cluster_b[2][1]]],

            [[cluster_a[0][0], cluster_b[0][0] - 1],
             [cluster_b[1][0], cluster_b[1][1]],
             [cluster_b[2][0], cluster_b[2][1]]],
            [[cluster_b[0][1] + 1, cluster_a[0][1]],
             [cluster_b[1][0], cluster_b[1][1]],
             [cluster_b[2][0], cluster_b[2][1]]]
        ])
    print('clusters', clusters)
    return clusters


def count_cubes(clusters: List[List[List[int]]]):
    total = 0
    return sum([reduce(lambda a, b: a * b, [1 + end - start for start, end in cluster]) for cluster in clusters])


def part_1(override_inputs = None):
    steps = get_inputs(parse_input) if override_inputs is None else override_inputs
    cleaned_steps = []

    boundary = 50

    for cmd, [[min_x, max_x], [min_y, max_y], [min_z, max_z]] in steps:
        if max(min_x, min_y, min_z) > boundary or min(max_x, max_y, max_z) < -1 * boundary:
            continue
        cleaned_steps.append((cmd, [[max(min_x, -1 * boundary), min(max_x, boundary)],
                                    [max(min_y, -1 * boundary), min(max_y, boundary)],
                                    [max(min_z, -1 * boundary), min(max_z, boundary)]]))

    clusters = []

    for cmd, new_cluster in cleaned_steps:
        new_clusters = []
        for cluster in clusters:
            verteces = [offset_vertex(new_cluster, vertex) for vertex in get_verteces(new_cluster)]
            new_clusters.extend(filter(lambda subcluster: not any(is_point_in_cluster(subcluster, vertex) for vertex in verteces),
                                split_cluster_at_verteces(cluster, verteces)))
            for subcluster in new_clusters:
                print(subcluster)

            # clusters_to_check = [cluster]
            # while clusters_to_check:
            #     cluster_to_check = clusters_to_check.pop()
            #     overlapping_verteces = [offset_vertex(new_cluster, vertex) for vertex in
            #                             filter(lambda vertex: is_point_in_cluster(cluster_to_check, vertex), verteces)]
            #     for vertex in overlapping_verteces:
            #         pass
        if cmd == 'on':
            new_clusters.append(new_cluster)
        clusters = new_clusters

    print(clusters)
    return count_cubes(clusters)


def part_2(override_inputs = None):
    steps = get_inputs(parse_input) if override_inputs is None else override_inputs

    print(steps)
    cubes = set()

    # for cmd, [[x1, x2], [y1, y2], [z1, z2]] in steps:
    #     print(cmd, [[x1, x2], [y1, y2], [z1, z2]])
    #     if cmd == 'on':
    #         for x in range(x1, x2 + 1):
    #             for y in range(y1, y2 + 1):
    #                 for z in range(z1, z2 + 1):
    #                     cubes.add((x, y, z))
    #     else:
    #         for x in range(x1, x2 + 1):
    #             for y in range(y1, y2 + 1):
    #                 for z in range(z1, z2 + 1):
    #                     cubes.discard((x, y, z))

    return len(cubes)


if __name__ == '__main__':
    print('Part 1:', part_1())
    print('Part 2:', part_2())
