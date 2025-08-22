# ceil in binary search tree

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def ceil(root, key):
    ceill = -1
    while root:
        if root.val == key:
            ceill = root.val
            return ceill   # exact match -> wahi ceil hai
        if key > root.val:
            root = root.right
        else:
            ceill = root.val  # possible ceil
            root = root.left
    return ceill


# Example tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

print("ceil: ", ceil(root, 11))  # Output -> 14
print("ceil: ", ceil(root, 5))   # Output -> 6
print("ceil: ", ceil(root, 2))   # Output -> 3
print("ceil: ", ceil(root, 15))  # Output -> -1 (not found)
