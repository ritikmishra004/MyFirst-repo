# min stack

class minStack:
    def __init__(self):
        self.stack = []
    def push(self,x):
        if not self.stack:
            self.stack.append((x,x))
        else:
            current_min = min((x,self.stack[-1][1]))
            self.stack.append((x,current_min))
    def pop(self):
        if not self.stack:
            return None
        return self.stack.pop()
    def top(self):
        if not self.stack:
            return None
        return self.stack[-1][0]
    def get_min(self):
        return self.stack[-1][1]
    
obj = minStack()
obj.push(5)
obj.push(2)
obj.push(8)
print(obj.get_min())  # ✅ 2
print(obj.top())     # ✅ 8
obj.pop()
print(obj.get_min())  # ✅ 2
print(obj.top())     # ✅ 2
obj.pop()
print(obj.get_min())  # ✅ 5