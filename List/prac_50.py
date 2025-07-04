# set matrix zeroes


def mark_row(matrix,column,i):
    for j in range(column):
        if matrix[i][j] != 0:
            matrix[i][j] = float('-inf')
def mark_column(matrix,rows,j):
    for i in range(rows):
        if matrix[i][j] != 0:
            matrix[i][j] = float('-inf')

def set_matrix(matrix,rows,column):
    for i in range(rows):
        for j in range(column):
            if matrix[i][j] == 0:
                mark_row(matrix,column,i)
                mark_column(matrix,rows,j)

    for i in range(rows):
        for j in range(column):
            if matrix[i][j]== float('-inf'):
                matrix[i][j] = 0

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

rows = len(matrix)
column = len(matrix[0])
set_matrix(matrix,rows,column)

for i in range(rows):
        for j in range(column):
            print(matrix[i][j],end=" ")
        print()