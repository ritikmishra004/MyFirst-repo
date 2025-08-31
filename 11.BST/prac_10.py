# Lowest common ancestor

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Function to find Lowest Common Ancestor (LCA)
def LCA(root, t1, t2):
    if not root:
        return None
    
    curr = root.val
    
    # ✅ Agar dono values root se badi hain -> LCA right subtree me hoga
    if curr < t1.val and curr < t2.val:
        return LCA(root.right, t1, t2)
    
    # ✅ Agar dono values root se chhoti hain -> LCA left subtree me hoga
    if curr > t1.val and curr > t2.val:
        return LCA(root.left, t1, t2)
    
    # ✅ Agar ek value left me aur ek right me hai -> yahi root LCA hai
    return root


# -----------------------
# Example usage:
root = None
for val in [20, 10, 30, 5, 15, 25, 35]:
    root = insert(root, val)

t1 = root.left.left      # 5
t2 = root.left.right     # 15

ans = LCA(root, t1, t2)
print("LCA:", ans.val)   # Output: 10
