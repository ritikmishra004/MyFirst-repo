# graph representaion 

# Graph Representation using Adjacency Matrix

# Step 1: Input number of nodes and edges
n, m = map(int, input("Enter number of nodes and edges (n m): ").split())

# Step 2: Initialize (n+1) x (n+1) matrix with 0
# +1 isliye taki 1-based indexing ke nodes easily use ho sakein
adj = [[0] * (n + 1) for _ in range(n + 1)]

# Step 3: Take m edges as input
print(f"Enter {m} edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u][v] = 1          # edge from u -> v
    adj[v][u] = 1          # undirected graph
    # agar graph directed hai to sirf u->v rakho (ye line hata do)

# Step 4: Print adjacency matrix
print("\nAdjacency Matrix:")
for row in adj[1:]:        # skip 0th row (since 1-based indexing)
    print(row[1:])         # skip 0th col
