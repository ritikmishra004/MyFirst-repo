# sort the linked list of 0's 1's 2's

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

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def sort_0_1_2(head):
    if head is None or head.next is None:
        return head  # Return as-is if list has 0 or 1 element

    # Create dummy heads for 0s, 1s, and 2s
    zero_head = Node(-1)
    one_head = Node(-1)
    two_head = Node(-1)

    # Create tails to build separate lists
    zero = zero_head
    one = one_head
    two = two_head

    temp = head

    # Distribute nodes into 3 lists
    while temp is not None:
        if temp.data == 0:
            zero.next = temp       # Zero list ke end mei current node jod do
            zero = zero.next       # Zero pointer ko aage badha do
        elif temp.data == 1:
            one.next = temp        # One list ke end mei current node jod do
            one = one.next         # One pointer ko aage badha do
        else:  # temp.data == 2
            two.next = temp        # Two list ke end mei current node jod do
            two = two.next         # Two pointer ko aage badha do
        temp = temp.next           # Original list mei aage badho

    # Connect the three lists together
    zero.next = one_head.next if one_head.next else two_head.next
    one.next = two_head.next
    two.next = None

    # Final head of sorted list
    return zero_head.next


arr = [1,2,0,1,2,0,1,2,0,1,1,2,2,0]
head = list_to_linkedList(arr)
print_list(head)
print("after")
head = sort_0_1_2(head)
print_list(head)