# set matrix zeroes
# optimal approach
# not done yet

def setZeroes(matrix):
    rows, cols = len(matrix), len(matrix[0])
    col0 = 1

    # 🔹 Step 1: Mark rows and columns to be zeroed
    for i in range(rows):
        if matrix[i][0] == 0:
            col0 = 0
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # 🔹 Step 2: Update the matrix (excluding first row & column)
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # 🔹 Step 3: Update first row if needed
    if matrix[0][0] == 0:
        for j in range(cols):
            matrix[0][j] = 0

    # 🔹 Step 4: Update first column if needed
    if col0 == 0:
        for i in range(rows):
            matrix[i][0] = 0

# 🔹 Example usage:
matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)
for row in matrix:
    print(row)
