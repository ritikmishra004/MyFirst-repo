# find maximum diameter between two node

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def diameter_of_tree(root):
    diameter = 0   # list use kar rahe hain taaki inner function isse update kar sake

    def height(node):
        nonlocal diameter # nonlocal is important... because int is immutable cant change from function 
        if not node:
            return 0

        # left aur right ki height
        lh = height(node.left)
        rh = height(node.right)

        # update diameter agar zarurat ho
        diameter = max(diameter, lh + rh)

        # height return karo
        return 1 + max(lh, rh)

    height(root)   # ek call se pura tree traverse hoga
    return diameter


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

print("Diameter: ", diameter_of_tree(root))
