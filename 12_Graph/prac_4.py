# Weighted Graph using Adjacency Matrix

# Step 1: Input number of nodes and edges
n, m = map(int, input("Enter number of nodes and edges (n m): ").split())

# Step 2: Initialize adjacency matrix with 0 (no edge)
adj_matrix = [[0] * (n + 1) for _ in range(n + 1)]  # n+1 for 1-based indexing

# Step 3: Input edges
print(f"Enter {m} edges in format: u v w (where w = weight):")
for _ in range(m):
    u, v, w = map(int, input().split())
    adj_matrix[u][v] = w   # u → v has weight w
    adj_matrix[v][u] = w   # undirected graph (remove for directed)

# Step 4: Print adjacency matrix
print("\nAdjacency Matrix (Weighted Graph):")
for row in adj_matrix[1:]:   # skip index 0
    print(row[1:])           # skip index 0
