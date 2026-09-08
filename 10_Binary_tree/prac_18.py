# Top view
# need multiple data structure like queue and list(dictionaries)
'''Har node ka ek horizontal distance (HD) hota hai root se.
Root ka HD = 0
Left child ka HD = parent_HD - 1
Right child ka HD = parent_HD + 1
Ek map/dictionary use karte hain (HD → Node) jisme sirf pehla node store karte hain jo us HD par aata hai.
BFS (queue) use karna best hai → kyunki level-wise traverse karte ho to sabse pehle dikhne wala node hi pick hoga.'''

from collections import deque

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def top_view(root):
    if not root:
        return []
    
    # Queue rakhenge (node, horizontal_distance) ke pair ke liye
    # root ki horizontal distance (hd) = 0 se start karte hain
    queue = deque([(root, 0)])  #...... queue = [(node, horizontal_distance)]
    
    # hd_map rakhega {horizontal_distance: node_value}
    # Sirf pehli baar jo hd milega usko store karenge (kyunki wo top view hoga)
    hd_map = {}
    
    # Level order traversal (BFS) karenge
    while queue:
        node, hd = queue.popleft()
        
        # Agar is hd pe pehle koi node store nahi hai
        # To current node hi top view me dikhega
        if hd not in hd_map:
            hd_map[hd] = node.data
        
        # Left child ko (hd-1) ke saath queue me dalte hain
        if node.left:
            queue.append((node.left, hd - 1))
        
        # Right child ko (hd+1) ke saath queue me dalte hain
        if node.right:
            queue.append((node.right, hd + 1))
    
    # hd_map ke keys ko sort karke unke corresponding nodes ka order banate hain
    result = [hd_map[x] for x in sorted(hd_map.keys())] 
    # x = -1 → hd_map[-1] = 2
    # x = 0 → hd_map[0] = 1
    # x = 1 → hd_map[1] = 3
    return result


# Example
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.right = Node(4)
root.left.right.right = Node(5)
root.left.right.right.right = Node(6)

print(top_view(root))  # Output: [2, 1, 3, 6]

'''def top_view(root):
    if not root:
        return []
    # queue = [(node, horizontal_distance)]
    queue = deque([(root, 0)])
    hd_map = {}
    while queue:
        node, hd = queue.popleft()
        if hd not in hd_map:
            hd_map[hd] = node.data
        if node.left:
            queue.append((node.left, hd-1))
        if node.right:
            queue.append((node.right, hd+1))
    result = [hd_map[x] for x in sorted(hd_map.keys())]
    return result'''