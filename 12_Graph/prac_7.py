# Number of Provinces (Connected Components in an Undirected Graph)

n, m = map(int, input("Enter number of nodes and edges (n m): ").split())

# adjacency list
adj = [[] for _ in range(n+1)]

print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)   # undirected graph

# DFS function
def dfs(node, visited):
    visited[node] = True
    for neighbour in adj[node]:
        if not visited[neighbour]:
            dfs(neighbour, visited)

# Function to count number of provinces
def no_of_provinces():
    visited = [False] * (n+1)
    cnt = 0
    for i in range(1, n+1):   # loop through all nodes
        if not visited[i]:    # agar node visited nahi hai
            cnt += 1          # ek naya province mila
            dfs(i, visited)   # us province ke sab nodes ko visit karo
    return cnt

# Run
print("Number of Provinces:", no_of_provinces())
