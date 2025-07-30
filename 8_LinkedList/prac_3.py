class Node:
    def __init__(self, data1, next1=None):
        self.data = data1      # data store kar raha
        self.next = next1      # next pointer (default None)

arr = [2, 5, 8, 7]             # Ek list banayi 4 elements ke saath

x = Node(arr[0], None)        # Node banaya jisme data = 2, next = None
y = x                         # y ab x ko point karta hai (same memory)

print(id(y))                  # y yaani x ka memory address print kar raha

print(id(x))