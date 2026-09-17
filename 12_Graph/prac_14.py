# 200. Number of Islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=cols:
                return 
            if grid[r][c]!="1":
                return
            grid[r][c]="0"
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc
                dfs(nr,nc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c]=="1":
                    count+=1
                    dfs(r,c)
        return count