# boundary traversal anti clockwise

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# ✅ check karna ki node leaf hai ya nahi
def is_leaf(root):
    if root.left is None and root.right is None:
        return True
    else:
        return False


# ✅ Left boundary (sirf non-leaf nodes)
def left_boundaries(root, res):
    curr = root.left
    while curr:   # left se niche jaate raho
        if not is_leaf(curr):   # leaf ko avoid karo (kyunki leaf baad me add honge)
            res.append(curr.data)
        if curr.left:
            curr = curr.left
        else:
            curr = curr.right

# ✅ Leaves (inorder traversal jaisa)
def leaf_boundaries(root, res):
    if is_leaf(root):
        res.append(root.data)
        return
    if root.left:
        leaf_boundaries(root.left, res)
    if root.right:
        leaf_boundaries(root.right, res)

# ✅ Right boundary (reverse order me store karna hai)
def right_boundaries(root, res):
    curr = root.right
    temp = []
    while curr:   # right se niche jaate raho
        if not is_leaf(curr):
            temp.append(curr.data)
        if curr.right:
            curr = curr.right
        else:
            curr = curr.left
    res.extend(temp[::-1])   # reverse karke add karo

# ✅ Final function jo order banayega
def boundary_traversal(root):
    res = []
    if not root:
        return res

    if not is_leaf(root):  # agar root leaf nahi hai to pehle root add karo
        res.append(root.data)

    left_boundaries(root, res)    # Step 1: Left boundary
    leaf_boundaries(root, res)    # Step 2: Leaf nodes
    right_boundaries(root, res)   # Step 3: Right boundary (reverse me)

    return res


# 🌳 Example tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(boundary_traversal(root))