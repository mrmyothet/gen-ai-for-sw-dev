import threading


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, max_size=None):
        self.head = None
        self.tail = None
        self.max_size = max_size
        self.size = 0
        self.lock = threading.Lock()

    def append(self, data):
        if len(data) > 1000:
            raise Exception("Data size exceeds maximum limit")

        with self.lock:
            if self.max_size and self.size >= self.max_size:
                raise Exception("List is full")

            new_node = Node(data)
            if not self.head:
                self.head = new_node
                self.tail = new_node
            else:
                self.tail.next = new_node
                self.tail = new_node
            self.size += 1

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
