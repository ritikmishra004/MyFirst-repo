# Reverse the doubly linked list

class Node:
    def __init__(self, data,next=None,back=None):
        self.data = data
        self.next = next
        self.back = back

def list_to_doubly(arr):
    if not arr:
        return None
    head = Node(arr[0])
    prev = head
    for value in arr[1:]:
        new_node = Node(value)
        prev.next = new_node       # connect forward
        new_node.back = prev       # connect backward
        prev = new_node
    return head

def print_linkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

# Reverse linked linst
def reverse_doubly(head):
    last = None
    current = head

    # Traverse the list until the end
    while(current != None):
        # Step 1: Store the previous pointer (will become next later)
        last = current.back

        # Step 2: Swap the 'next' and 'back' pointers
        current.back = current.next     # move 'back' to next node
        current.next = last             # move 'next' to previous node

        # Step 3: Move current to the next node in original order (which is now back)
        current = current.back
    # After loop ends, 'last' is at second last node, so we return last.back
    return last.back

arr = [1,2, 3, 4, 5, 6, 7]
head = list_to_doubly(arr)
print_linkedList(head)
print("After insertion")
head = reverse_doubly(head)
print_linkedList(head)
