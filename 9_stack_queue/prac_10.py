# min stack using 2 stack for minimum space complexity

class MinStack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self,x):
        self.stack.append(x)
        if not self.minstack or x<=self.minstack[-1]:
            self.minstack.append(x)
    def pop(self):
        if self.stack:
            if self.stack[-1] == self.minstack[-1]:
                self.minstack.pop()
        return self.stack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
        return None
    def get_min(self):
        return self.minstack[-1]
    def display(self):
        print(self.stack[::-1])

obj = MinStack()
obj.push(10)
obj.push(5)
obj.push(20)
print("Top:", obj.top())         # 20
print("Min:", obj.get_min())      # 5
print(obj.pop())
obj.display()
print("Top:", obj.top())         # 5
print("Min:", obj.get_min())      # 5
obj.pop()
print("Min:", obj.get_min())      # 10