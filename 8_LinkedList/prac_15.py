# delete tail in doubly linkedList

class Node:
    def __init__(self,data):
        self.data =data
        self.next = None
        self.back = None

def doubly_linkedList(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    prev =head

    for value in arr[1:]:
        new_node = Node(value)
        prev.next = new_node
        new_node.back = prev
        prev = new_node
    return head

def print_doubly(head):
    temp = head
    while(temp):
        print(temp.data,end = " <-> ")
        temp = temp.next
    print("None")

def deletion_in_doubly(head):
    tail = head                                # Step 1: Start from head
    while tail.next is not None:               # Step 2: Traverse to the last node (tail)
        tail = tail.next
    prev = tail.back                           # Step 3: Get second last node (previous of tail)
    prev.next = None                           # Step 4: Remove forward link from second last node
    tail.back = None                           # Step 5: Remove backward link from tail
    return head                                # Step 6: Return updated head (head remains same)

arr = [2,3,4,5,6,7]
head = doubly_linkedList(arr)
print_doubly(head)
print(" After deletion")
head = deletion_in_doubly(head)
print_doubly(head)
