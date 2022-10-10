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
    
    def shortest_distance(self, start, end):
        for neighbor in self.nodes[start].adjacent.keys():
            if neighbor == end:
                return self.nodes[start].adjacent[end]
        pass

    def dijkstra(self, start):
        dist = { start: 0 }
        prev = {}
        queue = PriorityQueue()

        for node in self.nodes:
            if node.id != start:
                dist[node.id] = math.inf
                prev[node.id] = None
            queue.add_item(node.id, dist[node.id])
        
        while not queue.is_empty():
            node = queue.pop()
            neighbors = self.nodes[node].adjacent
            for neighbor_id in neighbors.keys():
                if not queue.has_item(neighbor_id):
                    continue
                neighbor_distance = dist[node] + neighbors[neighbor_id]
                if neighbor_distance < dist[neighbor_id]:
                    dist[neighbor_id] = neighbor_distance
                    prev[neighbor_id] = node.id
                    queue.update_priority(neighbor_id, neighbor_distance)
        
        return dist


class Node:
    def __init__(self, id):
        self.id = id
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight):
        self.adjacent[neighbor] = weight
