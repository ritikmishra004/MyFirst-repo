# rotating the matrix by 90 degree

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

n = len(matrix)
# Step 1: Transpose the matrix
for i in range(n):
    for j in range(i+1, n):
        matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# Step 2: Reverse each row
for row in matrix:
    row.reverse()

print(matrix)