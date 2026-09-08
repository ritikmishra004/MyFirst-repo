# implement queue using array

class Queue:
    def __init__(self):
        self.queue = []

    # Enqueue (insert at end)
    def push(self, value):
        self.queue.append(value)

    # Dequeue (remove from front) – manually without pop()
    def pop(self):
        if not self.is_empty():
            value = self.queue[0]             # front element store karo
            self.queue = self.queue[1:]       # first element hata do
            return value
        else:
            return "Queue is empty"

    # Front element
    def top(self):
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



s = Queue()
s.push(5)
s.push(1)
s.push(2)
s.push(3)
s.display()
s.pop()
s.pop()
s.display()
print(s.pop())
print(s.top())
print(s.is_empty())
s.display()