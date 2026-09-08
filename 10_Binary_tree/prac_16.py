# Zig Zag traversal / spiral 

from collections import deque

from collections import deque

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def zigzag_traversal(root):
    if not root:
        return []

    # queue BFS ke liye
    queue = deque([root])  
    result = []

    # direction flag (True = Left→Right, False = Right→Left)
    left_to_right = True  

    while queue:
        size = len(queue)     # current level ke nodes ka count
        level = []            # is level ke nodes ko store karenge

        for _ in range(size):
            node = queue.popleft()   # queue se node nikalo
            level.append(node.data)  # level me add karo

            # child nodes ko queue me daal do (next level ke liye)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        # agar direction right→left hai to reverse kar do
        if not left_to_right:
            level.reverse()
        # is level ke nodes result me add kar do
        result.extend(level)
        # direction flip kar do next level ke liye
        left_to_right = not left_to_right  
    return result


# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print(zigzag_traversal(root))  

