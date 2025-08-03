# stack using array implementation

class Stack:
    def __init__(self):
        self.stack = []
    def push(self,value):
        self.stack.append(value)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "stack is empty"
    def top(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "stack is empty"
    def is_empty(self):
        return len(self.stack) == 0
    def size_of_stack(self):
        return len(self.stack)
    def display(self):
        print("stack (top to bottom)",self.stack[::-1])

s = Stack()
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