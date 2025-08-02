# reverse the linked list
# using stack

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

def reverse_linkedList(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp is not None:
        temp.data = stack.pop()
        temp = temp.next
    return head

arr = [1,2,3,4,5,6,7]
head = list_to_linkedList(arr)
print_list(head)
print("After")
head = reverse_linkedList(head)
print_list(head)