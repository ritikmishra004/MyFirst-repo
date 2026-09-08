# check if linkedList is palindrom

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

def palindrom(head):
    stack = []
    temp = head
    while temp:
        stack.append(temp.data)
        temp = temp.next
    temp = head
    while temp is not None:
        if temp.data != stack.pop():
            return False
        else:
            temp = temp.next
    return True

arr = [3,2,1,1,2,3]
head = list_to_linkedList(arr)
print_list(head)
print(palindrom(head))