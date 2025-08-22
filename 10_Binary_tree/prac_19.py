# Bottom level view of binary tree

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def bottom_view(root):
    if not root:
        return []
    
    # Queue -> store (node, horizontal distance)
    queue = deque([(root, 0)])
    hd_map = {}   # hd -> node.data (last seen at that hd)
    
    while queue:
        node, hd = queue.popleft()
        
        # For bottom view -> always update value
        hd_map[hd] = node.data
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Sort by horizontal distance and collect values
    result = [hd_map[x] for x in sorted(hd_map.keys())]
    return result


# 🌳 Example Tree
root = Node(20)
root.left = Node(8)
root.right = Node(22)
root.left.left = Node(5)
root.left.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(25)
root.left.right.left = Node(10)
root.left.right.right = Node(14)

print("Bottom View:", bottom_view(root))

    #      20
    #    /    \
    #   8      22
    #  / \    /  \
    # 5   3  4   25
    #    / \
    #   10 14

# for sorted mapp

# from collections import deque
# from sortedcontainers import SortedDict   # external library

# def bottom_view(root):
#     if not root:
#         return []
    
#     queue = deque([(root, 0)])
#     hd_map = SortedDict()   # automatically sorted by hd
    
#     while queue:
#         node, hd = queue.popleft()
#         hd_map[hd] = node.data   # overwrite (bottom view)
        
#         if node.left:
#             queue.append((node.left, hd - 1))
#         if node.right:
#             queue.append((node.right, hd + 1))
    
#     # direct values, no sorting needed
#     return list(hd_map.values())
