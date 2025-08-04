# implement queue using stack

from collections import deque
class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class Queue:
    def __init__(self):
        self.s1 = []  # Main stack
        self.s2 = []  # Helper stack

    # Enqueue (insert)
    def enqueue(self, value):
        # Step 1: Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Step 2: Push new element into s1
        self.s1.append(value)

        # Step 3: Move everything back from s2 to s1
        while self.s2:
            self.s1.append(self.s2.pop())

    # Dequeue (remove)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        return self.s1.pop()

    # Front element
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        return self.s1[-1]

    def is_empty(self):
        return len(self.s1) == 0

    def display(self):
        print("Queue (front to rear):", self.s1[::-1])

q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()         # Output: [10, 20, 30]
print(q.dequeue())  # Output: 10
q.display()         # Output: [20, 30]
