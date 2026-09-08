# symmetric or not

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def is_symmetric(root):
    if not root:
        return True
    
    def is_mirror(t1, t2):
        if not t1 and not t2:   # dono null → mirror
            return True
        if not t1 or not t2:    # ek null, ek non-null → not mirror
            return False
        return (t1.data == t2.data and 
                is_mirror(t1.left, t2.right) and 
                is_mirror(t1.right, t2.left))
    
    return is_mirror(root.left, root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

print("Symmetric: ", is_symmetric(root))

# using bfs
from collections import deque

def is_symmetric(root):
    if not root:
        return True
    
    queue = deque([(root.left, root.right)])
    
    while queue:
        t1, t2 = queue.popleft()
        
        if not t1 and not t2:
            continue
        if not t1 or not t2:
            return False
        if t1.data != t2.data:
            return False
        
        # mirror order me push karna hoga
        queue.append((t1.left, t2.right))
        queue.append((t1.right, t2.left))
    
    return True