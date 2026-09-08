class Node:
    def __init__(self, data, next_node=None):
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

def delete_tail(head):
    if head is None or head.next is None:
        return None
    
    temp = head
    while temp.next.next is not None:
        temp = temp.next
    
    # Now temp is second last node
    # del temp.next  # delete the tail node
    temp.next = None  # disconnect from list
    return head

def print_linkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next
    print("None")

# Driver code
arr = [2, 3, 5, 6, 9]
head = list_to_linkedList(arr)
print("Original linked list:")
print_linkedList(head)

head = delete_tail(head)
print("\nAfter deleting tail node:")
print_linkedList(head)
