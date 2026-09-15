#542. 01 Matrix

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows = len(mat)
        column = len(mat[0])
        queue = deque()
        dist = [[0]*column for _ in range(rows)]
        for r in range(rows):
            for c in range(column):
                if mat[r][c]==0:
                    queue.append((r,c))
                else:
                    dist[r][c]=-1

        direction = [(-1,0),(1,0),(0,-1),(0,1)]
        while queue:
            r,c = queue.popleft()
            for dr,dc in direction:
                nr = r+dr
                nc = c+dc
                if(0<=nr<rows and 0<=nc<column and dist[nr][nc]==-1):
                    dist[nr][nc]=dist[r][c]+1
                    queue.append((nr,nc))
        return dist