# BST iterator
# not done yet
#  dubara video dekho video 122

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# BST insert function
def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# ---- BST Iterator (functions only, no class) ----
stack = []   # global stack for traversal

def init_iterator(root):
    """Iterator initialize karne ke liye (leftmost nodes ko stack me daalo)"""
    while root:
        stack.append(root)
        root = root.left

def hasNext():
    """Check karega ki stack khali hai ya nahi"""
    return len(stack) > 0

def next():
    """Next smallest element return karega"""
    node = stack.pop()
    val = node.val
    # Agar right subtree hai to uske leftmost ko stack me daal do
    temp = node.right
    while temp:
        stack.append(temp)
        temp = temp.left
    return val


# ---------------- DRIVER CODE ----------------
# BST banate hain
root = None
preorder = [8, 5, 1, 7, 10, 12]
for v in preorder:
    root = insert(root, v)

# Iterator init
init_iterator(root)

# Iterator ka use
while hasNext():
    print(next(), end=" ")
