# doubly linkedList

# Node class for Doubly Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None       # forward pointer
        self.back = None       # backward pointer

# Function to convert array to Doubly Linked List
def convertArr2DLL(arr):
    if not arr: 
        return None  # agar array empty ho to

    head = Node(arr[0])   # pehla node create karo
    prev = head           # prev ko head pe point karwao

    for val in arr[1:]:
        # naye node ka creation
        new_node = Node(val)

        # previous node ka next, naye node ko point kare
        prev.next = new_node

        # naye node ka back, previous ko point kare
        new_node.back = prev

        # prev ko aage badhao
        prev = new_node

    return head  # DLL ka head return karo

# Function to print DLL
def printDLL(head):
    while head:
        print(head.data, end=" <-> ")
        head = head.next
    print("None")

# Example use
arr = [10, 20, 30, 40, 50]
head = convertArr2DLL(arr)
printDLL(head)