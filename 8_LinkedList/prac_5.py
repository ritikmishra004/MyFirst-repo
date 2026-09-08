# Create Node class
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Nodes banaye
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

# Connect nodes
n1.next = n2
n2.next = n3

# Pehle print (poori list)
print("Original Linked List:")
temp = n1
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")

# Delete head node
n1 = None      # Purane head ko delete kar diya
head = n2      # New head set kiya

# Print after deletion
print("After deleting head (10):")
temp = head
while temp:
    print(temp.data, end=" -> ")
    temp = temp.next
print("None")
