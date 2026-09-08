# check for balanced binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def balance_binary_tree(root):
    if not root:
        return 0
    
    lh = balance_binary_tree(root.left)
    rh = balance_binary_tree(root.right)

    # Agar koi subtree already unbalanced mila
    if lh == -1 or rh == -1:
        return -1

    # Agar left aur right height ka difference > 1 hai
    if abs(lh - rh) > 1:
        return -1

    # Otherwise height return karo
    return 1 + max(lh, rh)

# Example Tree
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.left.left = Node(7)
root.right.left.left.right = Node(8)
root.right.left.left.right.right = Node(9)

print("balanced binary tree: ", balance_binary_tree(root)!=-1)
