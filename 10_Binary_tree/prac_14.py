# Maximum path sum

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_path_sum(root):
    maxi = float('-inf')
    def max_sum(node):
        nonlocal maxi
        if not node:
            return 0
        lh = max_sum(node.left)
        rh = max_sum(node.right)
        maxi = max(maxi,lh+rh+node.data)

        return node.data+max(lh,rh)
    max_sum(root)
    return maxi

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

print("Max path sum: ", max_path_sum(root))
