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

def add_twoNumbers(l1, l2):
    dummy_node = Node(0)  # Dummy node banaya jisse hum result linked list banana start kar sakein
    current = dummy_node  # Current pointer ko dummy node pe set kiya
    carry = 0             # Pehle carry ko 0 se initialize kiya

    while l1 or l2 or carry:
        # Jab tak l1 ya l2 ya carry bacha ho, tab tak loop chalega

        value1 = l1.data if l1 else 0  # Agar l1 valid hai to uska data, warna 0
        value2 = l2.data if l2 else 0  # Agar l2 valid hai to uska data, warna 0

        total = value1 + value2 + carry  # Dono values + previous carry add karte hain
        carry = total // 10              # Naya carry calculate karte hain (e.g. 14 => carry = 1)
        current.next = Node(total % 10)  # Sirf unit digit nayi node mein store karte hain
        current = current.next           # Current pointer ko aage badha dete hain

        if l1:
            l1 = l1.next  # l1 ko aage le jaate hain
        if l2:
            l2 = l2.next  # l2 ko aage le jaate hain

    # ✅ Doubt: Carry ko explicitly last mein list mein kyun nahi joda?
    # ➤ Jab carry bacha hota hai (e.g. 1), to wo while condition mein 'carry' ki wajah se loop ek aur baar chalta hai.
    # ➤ value1 = 0, value2 = 0 hoga tab, total = carry hoga
    # ➤ total%10 ka ek aur node banega, aur carry 0 ho jayega.
    # ➤ Isliye last carry **automatically** result list mein jud jaata hai. Explicitly likhne ki zarurat nahi padti.

    return dummy_node.next  # Dummy node ke baad se hi actual result linked list start hoti hai

l1 = l1 = list_to_linkedList([3,5])
l2 = list_to_linkedList([4,5,9,9])
result = add_twoNumbers(l1, l2)
print_list(result)