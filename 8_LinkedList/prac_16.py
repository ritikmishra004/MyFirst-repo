# delete Kth node in doubly linked list

# Node class for doubly linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.back = None

# array ko doubly linked list mein convert karna
def list_to_doubly(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    prev = head

    for value in arr[1:]:
        new_node = Node(value)
        prev.next = new_node
        new_node.back = prev
        prev = new_node
    return head

# doubly linked list print karna
def print_linkedList(head):
    temp = head
    while temp:
        print(temp.data, end=" <-> ")
        temp = temp.next
    print("None")

# kth node delete karna
def delete_kth(head, k):
    if head is None:
        return None
    
    count = 0
    temp = head

    # kth node tak pahuchna
    while temp:
        count += 1
        if count == k:
            break
        temp = temp.next

    # 4 cases handle kar rahe hain niche:

    prev = temp.back
    front = temp.next

    # 1. sirf ek node hai
    if prev == None and front == None:
        temp = None
        return None

    # 2. head node delete ho rahi hai
    if prev == None and front != None:
        head = head.next
        head.back = None
        temp = None
        return head

    # 3. tail node delete ho rahi hai
    if prev != None and front == None:
        prev.next = None
        temp = None
        return head

    # 4. beech ki node delete ho rahi hai
    if prev != None and front != None:
        prev.next = front
        front.back = prev
        temp = None
        return head

# test
arr = [2, 3, 4, 5, 6, 7]
head = list_to_doubly(arr)
print_linkedList(head)
print("After deletion")
head = delete_kth(head, 4)
print_linkedList(head)
