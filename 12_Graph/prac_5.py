from collections import deque   # deque = double ended queue (fast for pop/append)

# Step 1: Input graph
n, m = map(int, input("Enter number of nodes and edges (n m): ").split())

# adjacency list representation
# [[] for _ in range(n+1)] => n+1 empty lists banenge
# index 0 ko ignore karte hain (1-based indexing ke liye)
adj = [[] for _ in range(n+1)]

print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)   # u -> v edge
    adj[v].append(u)   # v -> u edge (undirected graph)

# Step 2: BFS Function
def bfs(start):
    # visited array: taaki ek node ko bar-bar visit na karein
    visited = [False] * (n+1)

    # queue banai BFS ke liye
    q = deque()

    # starting node ko queue me daal do aur visited mark karo
    q.append(start)
    visited[start] = True

    # BFS order store karne ke liye list
    bfs_order = []

    # Jab tak queue khaali nahi hoti, tab tak process chalta rahega
    while q:
        node = q.popleft()        # queue se ek element nikala (FIFO)
        bfs_order.append(node)    # us node ko BFS result me add kar diya

        # ab uske saare neighbors ko check karo
        for neighbor in adj[node]:
            if not visited[neighbor]:    # agar neighbor pehle visit nahi hua
                q.append(neighbor)       # queue me dal do
                visited[neighbor] = True # visited mark kar do

    return bfs_order

# Step 3: Run BFS
start_node = int(input("Enter starting node: "))
print("BFS Traversal:", bfs(start_node))
