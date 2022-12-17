import math

from classes.PriorityQueue import PriorityQueue


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, id):
        if id not in self.nodes:
            self.nodes[id] = Node(id)

    def connect_nodes(self, start, end, weight, directional=False):
        self.nodes[start].add_neighbor(end, weight)
        if not directional:
            self.nodes[end].add_neighbor(start, weight)

    def dijkstra(self, start):
        D = {self.nodes[v].id: float('inf') for v in self.nodes}
        D[start] = 0
        prev = set()

        pq = PriorityQueue()
        pq.add_item((0, start), 0)

        while not pq.is_empty():
            (dist, current_vertex) = pq.pop()
            prev.add(current_vertex)

            for neighbor in self.nodes:
                if neighbor in self.nodes[current_vertex].adjacent.keys():
                    distance = self.nodes[current_vertex].adjacent[neighbor]
                    if neighbor not in prev:
                        old_cost = D[neighbor]
                        new_cost = D[current_vertex] + distance
                        if new_cost < old_cost:
                            pq.add_item((new_cost, neighbor), new_cost)
                            D[neighbor] = new_cost
        return D


class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight
