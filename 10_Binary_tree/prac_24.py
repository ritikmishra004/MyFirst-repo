# Lowest common Ancestor

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lca(root,t1,t2):
    if not root or root.val == t1 or root.val == t2:
        return root
    
    left = lca(root.left,t1,t2)
    right = lca(root.right,t1,t2)
    if not left:
        return right
    if not right:
        return left
    else:
        return root


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

ans = lca(root,5,8)
print("LCA:", ans.val if ans else None)
