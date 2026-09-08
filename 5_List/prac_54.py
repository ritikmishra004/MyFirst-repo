# rotating the matrix by 90 degree

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
rows = len(matrix)
column = len(matrix[0])
matrix_2 = [[0]*rows for _ in range(column)]
for i in range(rows):
    for j in range(column):
        matrix_2[j][rows-1-i]=matrix[i][j]
print(matrix_2)

# matrix[i][j]	→	matrix_2[j][rows - 1 - i]
# matrix[0][0] = 1	→	matrix_2[0][3] = 1
# matrix[0][1] = 2	→	matrix_2[1][3] = 2