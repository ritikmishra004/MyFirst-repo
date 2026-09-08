# DFS Traversal of Graph (Recursive)

# Step 1: Input graph
n, m = map(int, input("Enter number of nodes and edges (n m): ").split())

# adjacency list
adj = [[] for _ in range(n+1)]

print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)   # undirected graph

# Step 2: DFS function
def dfs(node, visited, dfs_order):
    visited[node] = True        # mark current node as visited
    dfs_order.append(node)      # add to result

    # visit all neighbors
    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, dfs_order)   # recursive call

# Step 3: Run DFS
visited = [False] * (n+1)
dfs_order = []

start_node = int(input("Enter starting node: "))
dfs(start_node, visited, dfs_order)

print("DFS Traversal:", dfs_order)
