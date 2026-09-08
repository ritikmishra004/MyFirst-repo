# set matrix zeroes
# better approach

def set_matrix(matrix,n,m):
    rows = [0]*n
    column = [0]*m
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows[i]=1
                column[j]=1
        
    for i in range(n):
        for j in range(m):
            if rows[i]==1 or column[j]==1:
                matrix[i][j]=0


matrix = [[0,2,1,0],[2,3,4,5],[9,8,7,6]]
n = len(matrix) # rows
m = len(matrix[0]) # column
set_matrix(matrix,n,m)

print(matrix)