# validate BST

# Node structure
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Function to validate BST
def isValidBST(root):
    def helper(node, low, high):
        # base case
        if not node:
            return True
        # agar node range break kar rahi hai to invalid
        if not (low < node.val < high):
            return False
        # left subtree ka max = node.val
        # right subtree ka min = node.val
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)

    return helper(root, float("-inf"), float("inf"))


# Tree bana rahe hain
root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
# root.right.left = Node(1)  # <-- agar ye add kar do to Invalid BST ho jaayega

print("Is Valid BST? ->", isValidBST(root))
