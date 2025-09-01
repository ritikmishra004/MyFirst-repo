# List representation 
# Adjacency List Representation in Python

# Step 1: Input nodes and edges
n, m = map(int, input("Enter number of nodes and edges (n m): ").split())

# Step 2: Initialize adjacency list (empty list for each node)
# Using dictionary for flexibility
adj = {i: [] for i in range(1, n+1)}

# Step 3: Take edges input
print("Enter edges (u v):")
for _ in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)   # add v in u's list
    adj[v].append(u)   # add u in v's list (because undirected)

# Step 4: Print adjacency list
print("\nAdjacency List:")
for node in adj:
    print(node, "->", adj[node])