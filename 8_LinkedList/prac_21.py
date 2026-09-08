# Reverse the doubly linked list

class Node:
    def __init__(self, data,next=None,back=None):
        self.data = data
        self.next = next
        self.back = back

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

def reverse_doubly(head):
    stack = []                      # Stack to hold node data
    temp = head

    # Push all node data to stack
    while temp is not None:
        stack.append(temp.data)
        temp = temp.next

    temp = head

    # Replace node data in reverse order
    while temp is not None:
        temp.data = stack.pop()     # Use pop() directly
        temp = temp.next

    return head


arr = [2, 3, 4, 5, 6, 7]
head = list_to_doubly(arr)
print_linkedList(head)
print("After insertion")
head = reverse_doubly(head)
print_linkedList(head)
