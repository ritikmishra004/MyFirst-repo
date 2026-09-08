# implement stack using queue

from collections import deque
class Node:
    def __init__(self,data):
        self.data =data
        self.next = None

class Stack:
    def __init__(self):
        self.q = deque()
    
    def push(self,x):
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
    
    def pop(self):
        if not self.is_empty():
            return self.q.popleft()
        else:
            return "Stack is empty"

    # Top element
    def top(self):
        if not self.is_empty():
            return self.q[0]
        else:
            return "Stack is empty"

    # Check if empty
    def is_empty(self):
        return len(self.q) == 0

    # Size
    def size(self):
        return len(self.q)

    # Display
    def display(self):
        print("Stack (top to bottom):", list(self.q))

s = Stack()
s.push(10)
s.push(20)
s.push(30)

s.display()        # Stack (top to bottom): [30, 20, 10]
print(s.pop())     # 30
print(s.top())     # 20
s.display()        # [20, 10]
