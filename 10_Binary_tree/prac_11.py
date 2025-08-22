# find maximum height

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_height(root):
    if not root:
        return 0
    lh = max_height(root.left)
    rh = max_height(root.right)

    return 1+max(lh,rh)


# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.left = Node(7)
root.right.left.left.right = Node(8)
root.right.left.left.right.right = Node(9)

print("maimum height: ", max_height(root))
