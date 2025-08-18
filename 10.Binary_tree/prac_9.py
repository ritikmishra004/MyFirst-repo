# BFS level print = [[1],[2,3],[4,5,6,7]]


from collections import deque

# Definition for a binary tree node.
class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def bfs(root):
        result = []
        if not root:
            return result
        
        queue = deque([root])   # start with root
        
        while queue:
            level = []                 # har level ke nodes
            for _ in range(len(queue)):  # current level ke saare nodes traverse karo
                node = queue.popleft()
                level.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            result.append(level)   # ek level complete hone ke baad add karo
        
        return result

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print(bfs(root))