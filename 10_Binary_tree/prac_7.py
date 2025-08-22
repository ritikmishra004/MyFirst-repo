# iterative inorder traversal
# using stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):
    inorder_result = []
    stack = []
    curr = root
    
    while curr or stack:
        # 1. Leftmost tak jao
        while curr:
            stack.append(curr)
            curr = curr.left
        
        # 2. Stack se pop karo (root)
        curr = stack.pop()
        inorder_result.append(curr.data)
        
        # 3. Right subtree ki taraf move karo
        curr = curr.right
    
    return inorder_result

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Function call
result = inorder(root)
print("Preorder Traversal:", result)
