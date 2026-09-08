# check if linkedList is palindrom
# do it again

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
    if not head or not head.next:
        return True  # 0 ya 1 node hai to hamesha palindrome hoti hai
    # Step 1: Tortoise-Hare to find middle of the linked list
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    # Step 2: Reverse second half of the list starting from 'slow'
    prev = None
    curr = slow
    while curr:
        front = curr.next
        curr.next = prev
        prev = curr
        curr = front
    # Ab 'prev' second half ka head hai (reversed list)

    # Step 3: Compare first half and reversed second half
    first = head
    second = prev
    while second:  # second half choti ya barabar hoti hai
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    
    return True


arr = [3,2,1,1,2,3]
head = list_to_linkedList(arr)
print_list(head)

print(palindrom(head))