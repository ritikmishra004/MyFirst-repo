# topological sort algorithm 

def topoSort(graph):
    n = len(graph)
    visited = [0]*n
    result = []

    def dfs(node):
        visited[node]=1
        for neighbour in graph[node]:
            if not visited[neighbour]:
                dfs(neighbour)
        result.append(node)

    for node in range(n):
        if not visited[node]:
            dfs(node)

    result.reverse()
    return result