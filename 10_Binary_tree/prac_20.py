# right/left view
# Using recursion

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def right_view_util(node, level, res):
    if not node:
        return
    
    # agar yeh level pehli baar visit ho raha hai
    if level == len(res):
        res.append(node.data)
    
    # pehle right side → then left side
    right_view_util(node.right, level + 1, res)
    right_view_util(node.left, level + 1, res)

def right_side_view(root):
    res = []
    right_view_util(root, 0, res)
    return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

print("Right Side View:", right_side_view(root))