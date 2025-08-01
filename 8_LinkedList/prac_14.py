# delete head in doubly linkedList

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

def delete_in_doubly(head):
    prev = head                     # Step 1: Store current head in 'prev' for disconnection
    head = head.next                # Step 2: Move head to the next node
    head.back = None                # Step 3: Remove backward reference from new head
    prev.next = None                # Step 4: Remove forward reference from old head
    return head                     # Step 5: Return new head


def print_doubly(head):
    temp = head
    while(temp):
        print(temp.data,end = " <-> ")
        temp = temp.next
    print("None")

arr = [2,3,4,5,6,7]
head = doubly_linkedList(arr)
print_doubly(head)
print(" After deletion")
head = delete_in_doubly(head)
print_doubly(head)