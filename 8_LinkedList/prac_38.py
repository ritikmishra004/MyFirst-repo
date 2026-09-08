# find the starting point of the loop

class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  

def find_starting(head):
    node_set = {}  # node ko store karne ke liye ek dictionary (hashmap) jahan key = node, value = index
    temp = head    # traversal ke liye temp pointer
    index = 0      # index track karne ke liye (loop kahan se start hua)

    while temp is not None:
        if temp in node_set:
            return node_set[temp]  # agar node pehle se set me hai to wahi loop ka start point hoga (index return karo)
            # return temp  # node_set[temp] ki jagah..Agar chaho to actual node bhi return kar sakte ho instead of index
        node_set[temp] = index     # nahi mila to node ko store kar lo dict me
        temp = temp.next           # next node pe jao
        index += 1                 # index badhao

    return "No loop"  # agar koi bhi loop nahi mila


if __name__ == "__main__":
    # Create a sample linked list with
    # a loop for testing
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth
    # Create a loop
    fifth.next = third
    
    print(find_starting(head))