# Python Linked Representation of binary tree
#   INORDER TRAVERSAL

class Node:
    def __init__(self,data,left= None,right=None):
        self.data = data
        self.left = left
        self.right = right

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

def inorder(node):
    if node:  
        inorder(node.left)         # Left child
        print(node.data, end=" ") # Current node
        inorder(node.right)        # Right child

# Output check
inorder(root)

'''NOTE Inorder Traversal
Type: DFS ka ek form
Order: Left → Root → Right
Kaam: Mostly Binary Search Tree (BST) me use hota hai taaki values sorted order me mil sake
Implementation: Recursion ya stack se
Complexity:
Time: O(n) → har node ek hi baar visit hoti hai
Space: O(h) → h = height of tree (recursion stack)

DFS ke 3 main types
Inorder → Left → Root → Right
Preorder → Root → Left → Right
Postorder → Left → Right → Root
BFS alag hota hai → Level by Level traversal (Queue use hota hai).'''