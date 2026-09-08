# Find minimum and maximum in bst

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mini(root):
    if not root:
        return None
    while root.left:
        root = root.left
    return root.val

def maxi(root):
    if not root:
        return None
    while root.right:
        root = root.right
    return root.val

# Example tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

print("minimun: ",mini(root))
print("maximum: ",maxi(root))