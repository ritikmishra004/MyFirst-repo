# iterative way of preorder traversal
# need stack to impliment it

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def it_pre(root):
    if not root:
        return []
    
    stack = [root]
    preorder = []   # yaha result store karenge
    
    while stack:
        node = stack.pop()
        preorder.append(node.data)  # print ke jagah list me daala
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return preorder   # finally list return karo

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Function call
result = it_pre(root)
print("Preorder Traversal:", result)
