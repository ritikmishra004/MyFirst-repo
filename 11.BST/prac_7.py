# Node definition
# kth smallest element
class Node:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


# Insert function to create BST
def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root


# Inorder Traversal helper
def inorder(root, result):
    if not root:
        return
    inorder(root.left, result)     # left
    result.append(root.val)        # root
    inorder(root.right, result)    # right


# Find k-th smallest in BST
def kthSmallest(root, k):
    result = []
    inorder(root, result)          # sorted list ban gaya
    if k <= len(result):
        return result[k-1]         # k-th smallest
    return None                    # agar k bada hai



# Create BST
root = None
values = [5,3,6,2,4,7]   # input values
for v in values:
    root = insert(root, v)

print("BST inorder (sorted):")
res = []
inorder(root, res)
print(res)

print("1st smallest:", kthSmallest(root, 1))
print("3rd smallest:", kthSmallest(root, 3))
print("5th smallest:", kthSmallest(root, 5))
