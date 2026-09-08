# delete node 


# Node structure for BST
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Function to insert node in BST (helper for building tree)
def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


# Function to find minimum value node (inorder successor)
def getMin(node):
    current = node
    while current.left:
        current = current.left
    return current


# Function to delete a node from BST
def deleteNode(root, key):
    # Base case: empty tree
    if not root:
        return root

    # Step 1: search for the node
    if key < root.val:
        root.left = deleteNode(root.left, key)   # left side search
    elif key > root.val:
        root.right = deleteNode(root.right, key) # right side search
    else:
        # Step 2: node found
        # Case 1: no child
        if not root.left and not root.right:
            return None
        # Case 2: only right child
        elif not root.left:
            return root.right
        # Case 3: only left child
        elif not root.right:
            return root.left
        # Case 4: two children
        else:
            successor = getMin(root.right)   # find inorder successor
            root.val = successor.val         # replace value
            root.right = deleteNode(root.right, successor.val) # delete successor
    
    return root


# Helper function to do inorder traversal (to check tree)
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)


# ----------------- Driver Code -----------------

# Create BST
root = None
values = [5,3,6,2,4,7]   # input tree values
for v in values:
    root = insert(root, v)

print("Inorder before deletion:", inorder(root))

# Delete node with value 3
root = deleteNode(root, 3)

print("Inorder after deletion :", inorder(root))
