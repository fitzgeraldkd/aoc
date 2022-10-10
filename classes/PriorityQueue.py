import math


class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def add_item(self, value, weight):
        self.items.append({ 'value': value, 'weight': weight })

    def pop(self):
        index = None
        min = { 'value': None, 'weight': math.inf }

        for i, item in enumerate(self.items):
            if item['weight'] < min['weight']:
                index = i
                min = item
        
        self.items.pop(index)
        return min['value']
    
    def is_empty(self):
        return len(self.items) == 0
    
    def has_item(self, check):
        for item in self.items:
            if item.value == check:
                return True
        return False
    
    def update_priority(self, value, weight):
        for item in self.items:
            if item['value'] == value:
                value['weight'] = weight