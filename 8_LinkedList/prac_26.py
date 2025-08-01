# sort the linked list of 0's 1's 2's

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

def sort_0_1_2(head):
    if not head:
        return None
    cnt_0 = 0
    cnt_1 = 0
    cnt_2 = 0
    temp = head
    while temp is not None:
        if temp.data == 0:
            cnt_0 += 1
        elif temp.data == 1:
            cnt_1 += 1
        else:
            cnt_2 += 1
        temp = temp.next
    temp = head
    while temp is not None:
        if cnt_0 != 0:
            temp.data = 0
            cnt_0 -= 1
        elif cnt_1 != 0:
            temp.data = 1
            cnt_1 -= 1
        elif cnt_2 != 0:
            temp.data = 2
            cnt_2 -= 1
        temp = temp.next
    return head

arr = [1,2,0,1,2,0,1,2,0,1,1,2,2,0]
head = list_to_linkedList(arr)
print_list(head)
print("after")
head = sort_0_1_2(head)
print_list(head)