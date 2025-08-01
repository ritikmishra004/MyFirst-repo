# inset in kth in dLL

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

def insert_head(head,node):
    # Step 1: Create new node with next as current head and back as None
    new_node = Node(node, head, None)
    
    # Step 2: If head is not None, update its back pointer to new_node
    if head:
        head.back = new_node
    # Step 3: Move head pointer to new_node
    head = new_node
    return head

def insert_at_kth(head, k, value):
    if k == 1:
        return insert_head(head, value)
    
    temp = head
    count = 1

    while temp and count < k - 1:
        temp = temp.next
        count += 1

    if temp is None:
        print("Position out of range")
        return head

    new_node = Node(value)
    new_node.next = temp.next
    new_node.back = temp

    if temp.next:
        temp.next.back = new_node

    temp.next = new_node

    return head

arr = [2, 3, 4, 5, 6, 7]
head = list_to_doubly(arr)
print_linkedList(head)
print("After insertion")
head = insert_at_kth(head, 4,10)
print_linkedList(head)