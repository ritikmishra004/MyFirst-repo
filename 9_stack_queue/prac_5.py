# Queue using linked list

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Queue class
class Queue:
    def __init__(self):
        self.start = None  # front
        self.end = None    # rear

    # Enqueue: insert at end
    def enqueue(self, value):
        new_node = Node(value)
        if self.end is None:
            self.start = self.end = new_node  # first element
        else:
            self.end.next = new_node
            self.end = new_node

    # Dequeue: remove from front
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        removed = self.start.data
        self.start = self.start.next
        if self.start is None:
            self.end = None  # queue becomes empty
        return removed

    # Peek front
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.start.data

    # Check if empty
    def is_empty(self):
        return self.start is None

    # Display
    def display(self):
        current = self.start
        print("Queue (front to rear):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

q.display()         # Queue (front to rear): 10 20 30
print(q.dequeue())  # 10
print(q.front())    # 20
q.display()         # 20 30
