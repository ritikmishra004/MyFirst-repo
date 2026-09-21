# Alien Dictionary

from collections import deque

class Solution:

    def findOrder(self, dict, N, K):

        graph = [[] for _ in range(K)]

        # Build graph
        for i in range(N - 1):

            word1 = dict[i]
            word2 = dict[i + 1]

            for j in range(min(len(word1), len(word2))):

                if word1[j] != word2[j]:

                    u = ord(word1[j]) - ord('a')
                    v = ord(word2[j]) - ord('a')

                    graph[u].append(v)

                    break

        # Calculate indegree
        indegree = [0] * K

        for u in range(K):
            for v in graph[u]:
                indegree[v] += 1

        # Kahn's Algorithm
        queue = deque()

        for i in range(K):
            if indegree[i] == 0:
                queue.append(i)

        result = []

        while queue:

            node = queue.popleft()

            result.append(chr(node + ord('a')))

            for neighbour in graph[node]:

                indegree[neighbour] -= 1

                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        # Cycle exists
        if len(result) != K:
            return ""

        return "".join(result)
