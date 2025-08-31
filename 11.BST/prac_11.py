# preorder construction of BST

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def preorder(root,val):
    if not root:
        return Node(val)
    if val < root.val:
        root.left = preorder(root.left,val)
    if val > root.val:
        root.right = preorder(root.right,val)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end =" ")
        inorder(root.right)

root = None
val = [8,5,1,7,10,12]
for v in val:
    root = preorder(root,v)

inorder(root)