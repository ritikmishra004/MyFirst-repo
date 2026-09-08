# Find the middle element of the node 

class Node:
    def __init__(self,data,next= None):
        self.data = data
        self.next = next

def list_to_linkedList(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head

    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_list(head):
    temp = head
    while(temp):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

def middle_node(head):
    slow = head
    fast = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
    prev_val = prev.data if prev else None
    next_val = slow.next.data if slow.next else None

    return prev_val, slow.data, next_val

arr = [1,2,3,4,5]
head = list_to_linkedList(arr)
print_list(head)
head = middle_node(head)
print(head)