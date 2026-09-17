# 785. Is Graph Bipartite?

class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [0]*n

        def dfs(node):
            for neighbour in graph[node]:
                if color[neighbour]==0:
                    color[neighbour]=3-color[node]
                    if not dfs(neighbour):
                        return False
                elif color[neighbour]== color[node]:
                    return False
            return True

        for node in range(n):
            if color[node]==0:
                color[node]=1
                if not dfs(node):
                    return False
        return True