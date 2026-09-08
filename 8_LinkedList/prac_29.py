# Remove the nth node from the linked list

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
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def remove_node(head, k):
    # Fast and slow pointers
    fast = head
    slow = head
    prev = None  # Slow ke pehle wali node

    # Step 1: Move fast pointer k steps aage
    # Yeh fast aur slow ke beech gap banata hai → |fast - slow| = k
    for _ in range(k):           #Yahan _ ka matlab hai: mujhe loop variable ki zarurat nahi, bas k baar repeat karna hai.
    # for _ in range(k): hum ye bhi use kar skte hain
        if fast is None:
            return head  # Agar k > length of list hai to kuch nahi karna
        fast = fast.next

    # Step 2: Agar fast None ho gaya → head node delete karni hai
    # Iska matlab: length = k
    if fast is None:
        return head.next  # Head hata diya

    # Step 3: Ab fast aur slow dono ko ek saath chalao
    # Jab fast end pe pahuchega (None), slow wahi node hoga jo delete karni hai
    # prev = slow se pehle wali node
    while fast:
        fast = fast.next
        prev = slow
        slow = slow.next

    # Step 4: Delete the slow node → skip kar do
    # prev.next → slow.next (slow node skip ho gaya)
    prev.next = slow.next

    return head


arr = [1,2,3,4,5,6,7]
head = list_to_linkedList(arr)
print_list(head)
print("After")
head = remove_node(head,4)
print_list(head)