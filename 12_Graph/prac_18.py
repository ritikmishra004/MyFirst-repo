# Topological Sorting Kahn's Algorithm

from collections import deque

def topoSort(graph):

    n = len(graph)

    indegree = [0] * n

    # Indegree calculate karo
    for node in range(n):
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    queue = deque()

    # Jinki indegree 0 hai
    for node in range(n):
        if indegree[node] == 0:
            queue.append(node)

    result = []

    while queue:

        node = queue.popleft()

        result.append(node)

        for neighbour in graph[node]:

            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    return result