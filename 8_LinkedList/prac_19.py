# inset in tail in dLL

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

def insert_in_tail(head,node):
    new_node = Node(node)
    if head is None:
        return None
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    new_node.back = temp
    return head

arr = [2, 3, 4, 5, 6, 7]
head = list_to_doubly(arr)
print_linkedList(head)
print("After insertion")
head = insert_in_tail(head, 4)
print_linkedList(head)
