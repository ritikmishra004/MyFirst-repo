# Sort linked list
# using sorting algorithm

class Node:
    def __init__(self,data,next = None):
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

def print_linkedList(head):
    if head is None and head.next is None:
        return head
    temp = head
    while temp:
        print(temp.data,end = " <-> ")
        temp = temp.next
    print("None")

def sort_linkedList(head):
    dummy_arr = []
    temp = head
    while temp is not None:
        dummy_arr.append(temp.data)
        temp = temp.next
    dummy_arr.sort()
    i = 0
    temp = head
    while temp is not None:
        temp.data = dummy_arr[i]
        i += 1
        temp = temp.next
    return head

arr = [3,9,5,8,1,6]
head = list_to_linkedList(arr)
print_linkedList(head)
print("After")
head = sort_linkedList(head)
print_linkedList(head)