# post order traversal 
# using 2 stack

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    stack_1 = [root]
    stack_2 = []
    result = []
    while stack_1:
        node = stack_1.pop()
        stack_2.append(node.data)

        if node.left:
            stack_1.append(node.left)
        if node.right:
            stack_1.append(node.right)
    while stack_2:
        result.append(stack_2.pop())
    return result

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# Function call
result = postorder(root)
print("postorder Traversal:", result)
