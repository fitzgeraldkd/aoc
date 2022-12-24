
class DoublyLinkedList:

    def __init__(self, data, close_loop = False):
        self.root = data
        self.next: DoublyLinkedList = self if close_loop else None
        self.prev: DoublyLinkedList = self if close_loop else None

    def append(self, data):
        new_node = DoublyLinkedList(data)
        next_node = self.next
        self.next = new_node
        new_node.prev = self

        if next_node is not None:
            next_node.prev = new_node
            new_node.next = next_node

        return new_node

    def prepend(self, data):
        new_node = DoublyLinkedList(data)
        prev_node = self.prev
        self.prev = new_node
        new_node.next = self

        if prev_node is not None:
            prev_node.next = new_node
            new_node.prev = prev_node

        return new_node

    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.next = None
        self.prev = None
        return self.root

    def length(self):
        length = 1
        current = self

        while current.next is not None and current.next != self:
            length += 1
            current = current.next

        return length
