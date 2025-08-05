# Implementing Queue using two Stacks (s1 and s2)

class Queue:
    def __init__(self):
        self.s1 = []  # Main stack that will always have the front element at the top
        self.s2 = []  # Temporary stack used for rearranging elements

    # Enqueue operation (Insert element in Queue)
    def enqueue(self, value):
        # Step 1: Move all elements from s1 to s2
        while self.s1:
            self.s2.append(self.s1.pop())

        # Step 2: Push the new value into s1 (now s1 is empty)
        self.s1.append(value)

        # Step 3: Move all elements back from s2 to s1
        # This ensures the front element remains at the top of s1
        while self.s2:
            self.s1.append(self.s2.pop())

    # Dequeue operation (Remove the front element)
    def dequeue(self):
        if self.is_empty():
            return "Queue is empty"
        # s1 has front element on top, simply pop it
        return self.s1.pop()

    # Get the front element without removing it
    def front(self):
        if self.is_empty():
            return "Queue is empty"
        # Last element in list is the front of queue
        return self.s1[-1]

    # Check if the queue is empty
    def is_empty(self):
        return len(self.s1) == 0

    # Display the queue from front to rear
    def display(self):
        # Reverse s1 to show queue in correct order
        print("Queue (front to rear):", self.s1[::-1])

# Testing the Queue
q = Queue()
q.enqueue(10)       # Queue becomes: [10]
q.enqueue(20)       # Queue becomes: [10, 20]
q.enqueue(30)       # Queue becomes: [10, 20, 30]
q.display()         # Output: Queue (front to rear): [10, 20, 30]

print(q.dequeue())  # Output: 10 is removed
q.display()         # Output: Queue (front to rear): [20, 30]
