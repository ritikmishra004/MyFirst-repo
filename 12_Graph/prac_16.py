# 210. Course Schedule II

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        graph=[[] for _ in range(numCourses)]
        
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
        result = []
        state = [0]*numCourses
        def dfs(course):
            if state[course]==1:
                return False
            if state[course]==2:
                return True
            state[course]=1
            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            state[course]=2
            result.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return result[::-1]