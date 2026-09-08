# length of loop in a linkedList

class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  

def length_of_loop(head):
    slow = head
    fast = head
    # Step 1: Use Floyd’s Cycle Detection Algorithm (Tortoise & Hare)
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        # Step 2: Cycle detected when slow meets fast
        if slow == fast:
            count = 1                  # ✅ count starts from 1 because we’re already at 1st loop node
            slow = slow.next          # move slow to next node
            # Step 3: Count how many nodes are in the loop
            while slow != fast:
                count += 1
                slow = slow.next
            return count              # return total loop length
    return None   # No cycle found


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
    
    print(length_of_loop(head))