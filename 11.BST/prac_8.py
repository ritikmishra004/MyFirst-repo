# Node definition
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


# Optimized k-th smallest (no extra list)
def kthSmallest(root, k):
    stack = []
    curr = root
    count = 0
    
    while stack or curr:
        # Leftmost tak jao
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # Node nikalo
        curr = stack.pop()
        count += 1
        if count == k:     # jaisi hi kth node mile
            return curr.val
        
        # Right subtree me jao
        curr = curr.right
    
    return None   # agar k > total nodes


# ---------------- Driver Code ----------------

root = None
values = [5,3,6,2,4,7]   # input values
for v in values:
    root = insert(root, v)

print("1st smallest:", kthSmallest(root, 1))  # 2
print("3rd smallest:", kthSmallest(root, 3))  # 4
print("5th smallest:", kthSmallest(root, 5))  # 6

# curr = curr.right ka matlab hai:

# Agar current node ke right child hai → uske leftmost tak jao next iterations me.
# Agar right child nahi hai → fir stack se upar ke nodes niklenge (ancestor nodes).

# ✅ Summary

# curr = curr.right isliye hai kyunki inorder traversal me root ke baad right subtree aata hai.
# Agar ye line hata denge, to hum kabhi right subtree visit hi nahi karenge → galat answer milega