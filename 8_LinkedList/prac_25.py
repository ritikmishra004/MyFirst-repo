# odd and even in linkedList

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

def odd_even(head):
    if not head or not head.next:
        return head  # Agar list mei 1 ya 0 node hai to waisa hi return karo

    odd = head                   # Odd pointer
    even = head.next            # Even pointer
    even_head = even            # Even list ka head preserve karo

    while even and even.next:
        odd.next = even.next    # Odd ke next mei agla odd node
        odd = odd.next          # Odd ko aage badhao
        even.next = odd.next    # Even ke next mei agla even node
        even = even.next        # Even ko aage badhao

    odd.next = even_head        # Odd list ke end mei even list jod do
    return head
arr = [1,2,3,4,5,6,7,8]
head = list_to_linkedList(arr)
print_list(head)
print("after")
head = odd_even(head)
print_list(head)