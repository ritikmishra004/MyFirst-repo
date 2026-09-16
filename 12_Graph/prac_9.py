# 207. Course Schedule
from collections import deque
from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
        
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
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True