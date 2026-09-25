class Solution:
    def shortestPath(self, N, M, edges):

        # 1. Graph banana
        graph = [[] for _ in range(N)]

        for u, v, weight in edges:
            graph[u].append((v, weight))

        # 2. DFS se Topological Sort
        visited = [False] * N
        stack = []

        def dfs(node):
            visited[node] = True

            for neighbour, weight in graph[node]:
                if not visited[neighbour]:
                    dfs(neighbour)

            # Neighbours complete hone ke baad
            stack.append(node)

        # Har node se DFS
        for node in range(N):
            if not visited[node]:
                dfs(node)

        # Reverse = Topological Order
        stack.reverse()

        # 3. Distance initialize
        INF = float('inf')
        dist = [INF] * N

        # Source = 0
        dist[0] = 0

        # 4. Topological order mein Relaxation
        for u in stack:

            # Agar source se reachable nahi hai
            if dist[u] == INF:
                continue

            for v, weight in graph[u]:

                # Relaxation
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

        # 5. Unreachable ko -1
        for i in range(N):
            if dist[i] == INF:
                dist[i] = -1

        return dist