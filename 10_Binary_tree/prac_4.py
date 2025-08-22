# implement BFS
from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def bfs(root):
    if not root:
        return
    queue = deque([root])

    while queue:
        node = queue.popleft()
        print(node.data,end = " ")
    
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

bfs(root)