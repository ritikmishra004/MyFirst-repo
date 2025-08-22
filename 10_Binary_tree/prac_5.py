from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bfs_level_wise(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        size = len(queue)   # current level ke nodes kitne hain
        for _ in range(size):
            node = queue.popleft()
            print(node.data, end=" ")
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        print()  # ek level khatam → new line

# Tree banaate hain
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

# BFS level-wise
bfs_level_wise(root)
