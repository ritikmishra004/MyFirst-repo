# Preorder traversal

class Node:
    def __init__(self,data,left= None,right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def preorder(node):
    if node:
        print(node.data,end=" ")
        preorder(node.left)
        preorder(node.right)

preorder(root)
