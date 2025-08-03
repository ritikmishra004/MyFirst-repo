# implement queue using array

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue (insert at end)
    def enqueue(self, value):
        self.queue.append(value)

    # Dequeue (remove from front)
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove first element
        else:
            return "Queue is empty"

    # Front element
    def front(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    # Check if queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Size of queue
    def size(self):
        return len(self.queue)

    # Display queue
    def display(self):
        print("Queue (front to rear):", self.queue)
