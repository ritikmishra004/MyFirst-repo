class Node:
    def __init__(self,data,next_node=None):
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
    temp = head
    while(temp):
        print(temp.data,end =" -> ")
        temp= temp.next
    print("None") 

# deleting head of linkedlist
def delete_head(head):
    if not head:
        return None
    temp = head
    head=head.next
    del temp
    return head

arr = [2,4,6,8]
head = list_to_linkedList(arr)
print_linkedList(head)
# after delete
head = delete_head(head)  # delete head
print("\nAfter deleting head node:")
print_linkedList(head)