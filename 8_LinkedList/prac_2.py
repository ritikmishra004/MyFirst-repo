# linkedList
class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

# Function to delete the tail of the linked list
def delete_tail(head):
    # Check if the linked list is empty or has only one node
    if head is None or head.next is None:
        return None

    # Create a temporary pointer for traversal
    temp = head

    # Traverse the list until the second-to-last node
    while temp.next.next is not None:
        temp = temp.next

    # Nullify the connection from the second-to-last node to delete the last node
    temp.next = None

    # Return the updated head of the linked list
    return head

# Function to print the linked list
def print_ll(head):
    while head is not None:
        print(head.data, end=" ")
        head = head.next

# Main function
if __name__ == "__main__":
    # Initialize an array with integer values
    arr = [2, 5, 8, 7]

    # Create the linked list with nodes initialized with array values
    head = Node(arr[0])
    head.next = Node(arr[1])
    head.next.next = Node(arr[2])
    head.next.next.next = Node(arr[3])

    # Delete the tail of the linked list
    head = delete_tail(head)

    # Print the modified linked list
    print_ll(head)
