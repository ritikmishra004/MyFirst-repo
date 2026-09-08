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
    if not head:
        return None

    dummy_node = Node(0)  # Dummy node to start result list
    current = dummy_node

    temp = head
    # Pehle odd position wale nodes daalo
    while temp is not None and temp.next is not None:
        current.next = Node(temp.data)
        current = current.next
        temp = temp.next.next
    if temp:  # Agar list odd length ki ho, to last odd node ko bhi add karo
        current.next = Node(temp.data)
        current = current.next

    temp = head.next
    # Ab even position wale nodes daalo
    while temp and temp.next:
        current.next = Node(temp.data)
        current = current.next
        temp = temp.next.next
    if temp:  # Agar even nodes last mei bache ho to unhe bhi add karo
        current.next = Node(temp.data)

    return dummy_node.next  # dummy ka next hi actual head hai


arr = [1,2,3,4,5,6,7,8]
head = list_to_linkedList(arr)
print_list(head)
print("after")
head = odd_even(head)
print_list(head)