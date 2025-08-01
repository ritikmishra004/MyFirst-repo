# delete node

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

def list_to_doubly(arr):
    # Convert array to doubly linked list
    if not arr:
        return None
    head = Node(arr[0])
    prev = head
    for value in arr[1:]:
        new_node = Node(value)
        prev.next = new_node       # connect forward
        new_node.back = prev       # connect backward
        prev = new_node
    return head

def print_linkedList(head):
    # Print linked list from head to tail
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

def find_node_by_value(head, value):
    # Traverse and return the node with matching value
    temp = head
    while temp:
        if temp.data == value:
            return temp
        temp = temp.next
    return None  # Value not found

def remove_node(head, node):
    # Remove a given node from DLL
    if node is None:
        return head

    if node.back is None:
        # If it's the head node
        head = node.next
        if head:
            head.back = None
    elif node.next is None:
        # If it's the tail node
        node.back.next = None
    else:
        # If it's a middle node
        node.back.next = node.next
        node.next.back = node.back

    # After unlinking, Python GC will delete it if no reference
    node = None
    return head

# Main
arr = [2, 3, 4, 5, 6, 7]
head = list_to_doubly(arr)                 # Create DLL from array
print("Before deletion:")
print_linkedList(head)                     # Print original list

node_to_delete = find_node_by_value(head, 4)  # Locate node with value 4
head = remove_node(head, node_to_delete)      # Delete that node

print("After deleting node with value 4:")
print_linkedList(head)                     # Print updated list
