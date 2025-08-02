# length of loop in a linkedList

class Node:
    def __init__(self, data, next_node=None):
        self.data = data       
        self.next = next_node  

def length_of_loop(head):
    visited = {}  # Dictionary to store node → index
    temp = head
    index = 0     # Index to track node position

    while temp:
        if temp in visited:
            loop_start_index = visited[temp]       # Where loop started
            return index - loop_start_index        # Distance = loop length
        visited[temp] = index                      # Mark this node visited
        temp = temp.next
        index += 1

    return 0  # Agar loop nahi mila to


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