# reverse the linked list

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
    if head is None or head.next is None:  # Agar list empty hai ya ek hi node hai
        return head

    front = None      # Ye temp ke next ko hold karega
    prev = None       # Reversed list ka pehla node banega ye
    temp = head       # Current node jisko hum process kar rahe hain

    while temp is not None:
        front = temp.next     # Next node ko store karo (taaki link toot na jaye)
        temp.next = prev      # Current node ka next ab previous node banega
        prev = temp           # Prev ko current pe shift karo
        temp = front          # Temp ko aage badhao

    return prev               # Prev ab new head hai reversed list ka



arr = [1,2,3,4,5,6,7]
head = list_to_linkedList(arr)
print_list(head)
print("After")
head = reverse_linkedList(head)
print_list(head)