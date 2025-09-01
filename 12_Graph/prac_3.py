# Weighted Graph using Adjacency List

# Step 1: Input number of nodes and edges
n, m = map(int, input("Enter number of nodes and edges (n m): ").split())

# Step 2: Initialize adjacency list
# Har node ke liye ek empty list
adj = [[] for _ in range(n + 1)]   # n+1 isliye taki 1-based indexing use ho sake

# Step 3: Input edges
print(f"Enter {m} edges in format: u v w (where w = weight):")
for _ in range(m):
    u, v, w = map(int, input().split())
    adj[u].append((v, w))   # u → v with weight w
    adj[v].append((u, w))   # undirected graph ke liye (remove for directed)
    
# Step 4: Print adjacency list
print("\nAdjacency List (Weighted Graph):")
for i in range(1, n + 1):
    print(f"{i} → {adj[i]}")
