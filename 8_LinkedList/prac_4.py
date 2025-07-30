# Step 1: Node class - ek single node define karta hai (data + pointer to next)
class Node:
    def __init__(self, data):
        self.data = data      # Node ke andar value store hoti hai
        self.next = None      # By default next pointer null hota hai

# Step 2: List to Linked List conversion function
def list_to_linkedlist(arr):
    if not arr:
        return None           # Agar list empty hai toh koi node banane ki zarurat nahi

    head = Node(arr[0])       # Pehla element ka node banake usse head set kar diya
    current = head            # 'current' pointer banaya jo naya node attach karega

    for value in arr[1:]:     # Baaki sab elements ke liye loop
        current.next = Node(value)  # Naya node banaya aur current se link kiya
        current = current.next      # Current pointer ko aage badhaya

    return head               # Head return kiya jo pura linked list ka starting point hai

# Step 3: Print function for Linked List
def print_linkedlist(head):
    temp = head
    while temp:
        print(temp.data, end=" -> ")  # Har node ka data print karo
        temp = temp.next              # Aage badho next node pe
    print("None")                     # Jab last tak pahuch jao toh None print karo

def get_length(head):
    count = 0                  # Counter start from 0
    temp = head                # temp pointer ko head pe set kiya

    while temp:                # Jab tak temp None nahi ho jata
        count += 1             # Node mila toh count badhao
        temp = temp.next       # temp ko next node pe le jao

    return count               #  Final count return karo

#search
def checkIfPresent(head,value):
    temp = head
    while temp:
        if temp.data == value:
            return 1
        temp = temp.next              # Aage badho next node pe
    return 0  

# Example usage:
arr = [2, 5, 8, 7]              # Input list
head = list_to_linkedlist(arr) # List ko Linked List mein convert kiya
print_linkedlist(head)         # Linked List print kiya

length = get_length(head)
print("Length of linked list:", length)
print(checkIfPresent(head,5))