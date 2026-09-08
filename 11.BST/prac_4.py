# floor in binary search tree

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def floor(root, key):
    flr = -1
    while root:
        if root.val == key:
            flr = root.val
            return flr
        if key > root.val:
            flr = root.val
            root = root.right
        else:
            root = root.left
    return flr


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

print("floor: ", floor(root, 11)) 
print("floor: ", floor(root, 5))
print("floor: ", floor(root, 2))
print("floor: ", floor(root, 15))
