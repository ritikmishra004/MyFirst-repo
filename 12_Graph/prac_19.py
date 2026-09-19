# 802. Find Eventual Safe States
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:

        n = len(graph)
        state = [0] * n

        def dfs(node):

            # Current DFS path mein already hai
            if state[node] == 1:
                return False

            # Already checked and safe
            if state[node] == 2:
                return True

            # Currently visiting
            state[node] = 1

            for neighbour in graph[node]:

                if not dfs(neighbour):
                    return False

            # Saare neighbours safe hain
            state[node] = 2

            return True

        result = []

        for node in range(n):

            if dfs(node):
                result.append(node)

        return result