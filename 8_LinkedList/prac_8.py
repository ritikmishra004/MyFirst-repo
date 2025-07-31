# deleting kth element from the linkedList

# Node class bana rahe hain jisme data aur next pointer store hoga
class Node:
    def __init__(self,data,next_node=None):
        self.data = data
        self.next = next_node

# List ko linked list mein convert karne ka function
def list_to_linkedList(arr):
    if not arr:
        return None
    
    head = Node(arr[0])   # Pehla node head hoga
    current = head

    for value in arr[1:]:  # Baaki elements ke liye next nodes create kar rahe hain
        current.next = Node(value)
        current = current.next
    return head

# Kth node ko delete karne ka function
def delete_Kth(head,k):
    if head == None:
        return head
    if k == 1:  # Agar pehla element delete karna hai
        temp = head
        head = head.next  # head ko aage shift kar do
        del temp          # purane head ko delete kar do
        return head
    cnt = 0
    temp = head
    previous = None
    while(temp != None):
        cnt += 1
        if cnt == k:
            previous.next = previous.next.next  # Kth node ko link se hata rahe hain
            del temp                            # memory se delete
            break
        previous = temp
        temp = temp.next
    return head

# Linked list ko print karne ka function
def print_linkedList(head):
    temp = head
    while(temp):
        print(temp.data,end=" -> ")  # har node ka data print kar rahe hain
        temp = temp.next
    print("None")

# Driver code
arr = [9,8,7,6,5,4,23,4]
k = 3
head = list_to_linkedList(arr)
print_linkedList(head)
print("After deletion ")
delete_Kth(head,k)
print_linkedList(head)