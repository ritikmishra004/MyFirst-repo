# insertion in kth position

class Node:
    def __init__(self,data,next_node = None):
        self.data = data
        self.next = next_node

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
    if not head:
        return None
    temp = head
    while(temp):
        print(temp.data,end=" -> ")
        temp = temp.next
    print("None")

# insertion
def insert_in_Kth(head,k,value):
    if head == None:
        return None
    if k == 1:
        temp = Node(value,head)
        return temp
    count = 0
    temp = head
    while(temp!=None):
        count += 1
        if count == k-1:
            x = Node(value)
            x.next = temp.next
            temp.next = x
            break
        temp = temp.next
    return head

arr = [2,3,4,5,6,7]
head = list_to_linkedList(arr)
print_linkedList(head)
head = insert_in_Kth(head,3,12)
print("After insertion")
print_linkedList(head)
