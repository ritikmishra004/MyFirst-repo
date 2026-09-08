# implement stack using linked list

class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    def push(self,x):
        new_node = Node(x)
        new_node.next = self.top
        self.top = new_node
    def pop(self):
        if self.is_empty():
            return "stack is empty"
        temp = self.top.data
        self.top = self.top.next
        return temp
    def peek(self):
        if self.is_empty():
            return "stack is empty"
        return(self.top.data)
    def is_empty(self):
        return self.top is None
    def display(self):
        current = self.top
        print("Stack (top to bottom):", end=" ")
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

s = Stack()
s.push(9)
s.push(19)
s.push(2)
s.push(5)
s.push(8)
s.display()
s.pop()
s.pop()
s.display()
print(s.is_empty())
s.pop()
s.display()  
print(s.pop())   
print(s.peek())  
s.display()      