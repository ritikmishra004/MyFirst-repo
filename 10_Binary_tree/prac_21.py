# right/left side view using bfs
# Not done yet

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def right_side_view(root):
    if not root:
        return []
    
    res = []
    queue = deque([root])
    
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            
            # last node of this level → right view
            if i == size - 1:
                res.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


def left_side_view(root):
    if not root:
        return []
    
    res = []
    queue = deque([root])
    
    while queue:
        size = len(queue)
        for i in range(size):
            node = queue.popleft()
            
            # first node of this level → left view
            if i == 0:
                res.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return res


# 🔹 Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(5)
root.right.right = Node(4)

print("Right Side View:", right_side_view(root))  # [1, 3, 4]
print("Left Side View:", left_side_view(root))    # [1, 2, 5]
