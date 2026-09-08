# insertion in last

class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next = next_node

def list_to_linkedList(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

def print_linkedList(head):
    if not head:
        return None
    temp = head
    while(temp):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

# insertion
def insertion(head,value):
    new_node = Node(value)
    if head is None:
        return new_node
    temp = head
    while temp.next is not None:
        temp = temp.next
    temp.next = new_node
    return head

arr = [2,3,4,5,6,7]
value = 10
head = list_to_linkedList(arr)
print_linkedList(head)
head = insertion(head,value)
print("After insertion")
print_linkedList(head)
