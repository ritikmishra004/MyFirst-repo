# 1020. Number of Enclaves

from typing import List
class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        column = len(grid[0])
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        count=0

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=column:
                return
            if grid[r][c]!=1:
                return
            grid[r][c]=0
            for dr,dc in directions:
                nr =r+dr
                nc =c+dc
                dfs(nr,nc)
        for c in range(column):
            if grid[0][c]==1:
                dfs(0,c)
            if grid[rows-1][c]==1:
                dfs(rows-1,c)
        for r in range(rows):
            if grid[r][0]==1:
                dfs(r,0)
            if grid[r][column-1]==1:
                dfs(r,column-1)
        for r in range(rows):
            for c in range(column):
                if grid[r][c]==1:
                    count+=1
        return count
