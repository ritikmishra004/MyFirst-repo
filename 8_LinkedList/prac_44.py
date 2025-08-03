# Sort linked list
# using sorting algorithm

class Node:
    def __init__(self,data,next = None):
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

def print_linkedList(head):
    if head is None or head.next is None:
        return head
    temp = head
    while temp:
        print(temp.data,end = " <-> ")
        temp = temp.next
    print("None")

# Function to find the middle node of the linked list
def find_middle(head):
    slow = head
    fast = head.next  # Start fast one step ahead for even-length handling
    while fast and fast.next:
        slow = slow.next  # Move slow by 1
        fast = fast.next.next  # Move fast by 2
    return slow  # When fast reaches end, slow is at middle


# Function to merge two sorted linked lists
def merge(left, right):
    dummy_node = Node(0)  # Dummy node to simplify merging
    tail = dummy_node  # Tail pointer to build the merged list

    # Merge while both lists have elements
    while left and right:
        if left.data < right.data:
            tail.next = left  # Attach smaller node
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next  # Move tail forward

    # Attach remaining nodes (only one of them will be non-empty)
    tail.next = left or right

    return dummy_node.next  # Return head of merged list (after dummy)


# Main function to sort the linked list using merge sort
def sort_linkedList(head):
    # Base case: 0 or 1 node is already sorted
    if head is None or head.next is None:
        return head

    # Step 1: Split the list into two halves
    middle = find_middle(head)
    right = middle.next  # Start of right half
    middle.next = None   # Break the list into two parts
    left = head          # Start of left half

    # Step 2: Recursively sort the left and right halves
    left = sort_linkedList(left)
    right = sort_linkedList(right)

    # Step 3: Merge the sorted halves
    return merge(left, right)


arr = [3, 9, 5, 8, 1, 6]
head = list_to_linkedList(arr)
print("Before sorting:")
print_linkedList(head)

print("\nAfter sorting:")
head = sort_linkedList(head)
print_linkedList(head)