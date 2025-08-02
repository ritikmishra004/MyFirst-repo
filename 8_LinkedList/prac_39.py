# find the starting point of the loop

class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  

def find_starting(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = head
            index = 0
            while slow != fast:
                slow = slow.next
                fast = fast.next
                index+=1
            return index
    return None

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