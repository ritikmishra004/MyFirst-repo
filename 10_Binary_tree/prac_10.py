# postorder iterative
# using 2 stack


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def postorder(root):
    result = []
    stack = []
    last_visited = None
    current = root

    while stack or current:
        if current:  # 1. leftmost tak jao
            stack.append(current)
            current = current.left
        else:
            peek = stack[-1]  # stack ka top dekho (pop mat karo abhi)
            # 2. agar right child hai aur wo last visited nahi hai
            if peek.right and last_visited != peek.right:
                current = peek.right
            else:
                # 3. otherwise root ko visit karo
                result.append(peek.data)
                last_visited = stack.pop()
    
    return result

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("Postorder Traversal:", postorder(root))
