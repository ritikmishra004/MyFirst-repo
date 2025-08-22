# root to Node path

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def root_to_node_path(node, target):
    path = []

    def dfs(node):
        if not node:
            return False

        # step 1: current node ko path me add karo
        path.append(node.val)

        # step 2: agar target mil gaya
        if node.val == target:
            return True

        # step 3: left ya right subtree me search karo
        if dfs(node.left) or dfs(node.right):
            return True

        # step 4: backtrack (agar target yaha se nahi mila to remove karo)
        path.pop()
        return False
    dfs(node)
    return path

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.left.left.left = Node(8)

print("PATH: ", root_to_node_path(root,8))
