# Remove the nth node from the linked list

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

def remove_node(head, k):
    if head is None:
        return None  # agar list empty ho to kuch karne ki zarurat nahi

    cnt = 0
    temp = head
    while temp is not None:
        cnt += 1             # total nodes count kar rahe hain
        temp = temp.next

    new = cnt - k           # jis node ko remove karna hai usse pehle wale tak jaana hai

    if new == 0:
        return head.next    # agar head node hi delete karni hai to uska next return kar do

    temp = head
    while temp is not None:
        new -= 1
        if new == 0 and temp.next is not None:
            temp.next = temp.next.next  # node ko skip kar diya
            break
        temp = temp.next

    return head

arr = [1,2,3,4,5,6,7]
head = list_to_linkedList(arr)
print_list(head)
print("After")
head = remove_node(head,4)
print_list(head)