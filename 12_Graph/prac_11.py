# 130. Surrounded Regions

class Solution:
    def solve(self, board: list[list[str]]) -> None:
        rows = len(board)
        column = len(board[0])

        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(r,c):
            if r<0 or r>=rows or c<0 or c>=column:
                return
            if board[r][c]!='O':
                return
            board[r][c]='#'
            for dr,dc in directions:
                nr = r+dr
                nc = c+dc

                dfs(nr,nc)
        #top/bottom
        for c in range(column):
            if board[0][c]=="O":
                dfs(0,c)
            if board[rows-1][c]=="O":
                dfs(rows-1,c)
        #left/right
        for r in range(rows):
            if board[r][0]=="O":
                dfs(r,0)
            if board[r][column-1]=="O":
                dfs(r,column-1)
        #convert
        for r in range(rows):
            for c in range(column):
                if board[r][c]=="O":
                    board[r][c]="X"
                if board[r][c]=="#":
                    board[r][c]="O"