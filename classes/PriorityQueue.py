class PriorityQueue:
    def __getitem__(self, i):
        return self.items[i]['value']

    def __init__(self):
        self.items = []
    
    def __iter__(self):
        return iter(map(lambda item: item['value'], self.items))

    def __len__(self):
        return len(self.items)
    
    def add_item(self, value, weight):
        new_item = {'value': value, 'weight': weight}
        for index, item in enumerate(self.items):
            if weight > item['weight']:
                self.items.insert(index, new_item)
                return value
        
        self.items.append(new_item)
        return value

    def pop(self):
        item = self.items.pop()
        return item['value']
    
    def is_empty(self):
        return len(self.items) == 0
    
    def has_item(self, check):
        for item in self.items:
            if item['value'] == check:
                return True
        return False
    
    def update_priority(self, value, weight):
        for index, item in enumerate(self.items):
            if item['value'] == value:
                self.items.pop(index)
                self.add_item(value, weight)
                break
