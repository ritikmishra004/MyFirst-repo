# insertion in front

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

# insertion
def insert_in_list(head,value):
    temp = Node(value,head)
    return temp

def print_linkedList(head):
    if not head:
        return None
    temp = head
    while(temp):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

arr = [2,3,4,5,6,7]
value = 10
head = list_to_linkedList(arr)
print_linkedList(head)
head = insert_in_list(head,value)
print_linkedList(head)