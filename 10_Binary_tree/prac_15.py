class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

def is_identical(node1, node2):
    # dono null -> same
    if not node1 and not node2:
        return True
    # ek null aur dusra nahi -> different
    if not node1 or not node2:
        return False
    # dono non-null -> check data + children
    return (node1.data == node2.data and 
            is_identical(node1.left, node2.left) and 
            is_identical(node1.right, node2.right))


# Example trees
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

root_1 = Node(1)
root_1.left = Node(2)
root_1.right = Node(3)
root_1.left.left = Node(4)
root_1.left.right = Node(5)
root_1.right.left = Node(6)
root_1.right.right = Node(7)

print(is_identical(root, root_1))   # ✅ True