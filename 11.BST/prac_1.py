# search in binary search tree

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def search_bst(root, target):
    if not root:
        return None  
    
    if root.val == target:
        # yahan left aur right check karenge
        left_val = root.left.val if root.left else None
        right_val = root.right.val if root.right else None
        return (root.val, left_val, right_val)
    
    if target < root.val:
        return search_bst(root.left, target)
    else:
        return search_bst(root.right, target)


# Example tree
root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)

# Test
result = search_bst(root, 3)
if result:
    print("Found:", result)   # (node, left, right)
else:
    print("Not Found")

# Ab node2 ke andar:

# val = 2
# left = node1 (value 1)
# right = node3 (value 3)
# Agar main sirf node2 ko return karun, to actually main pura subtree return kar raha hoon: