# Insert new Node in bst

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def insert_node(root,val):
    curr = root
    while True:
        if curr.val <= val:
            if curr.right != None:
                curr = curr.right
            else:
                curr.right = Node(val)
                break
        else:
            if curr.left != None:
                curr = curr.left
            else:
                curr.right = Node(val)
                break

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end =" ")
        inorder(root.right)

root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
insert_node(root,15)
inorder(root)
