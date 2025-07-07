# spiral matrix

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(matrix) # rows
m = len(matrix[0]) # column 
# defining boundaries
left = 0
right = m-1
top = 0
bottom = n-1
ans = []
# 🔁 Jab tak saari boundaries valid hain tab tak chalao
while top <= bottom and left <= right:
    
    # 🔹 Step 1: Left → Right (Top row traverse karo)
    for i in range(left, right + 1):
        ans.append(matrix[top][i])
    top += 1  # ✅ Top boundary ko ek row niche le jao

    # 🔹 Step 2: Top → Bottom (Rightmost column)
    for i in range(top, bottom + 1):
        ans.append(matrix[i][right])
    right -= 1  # ✅ Right boundary ko ek column left le jao

    # 🔹 Step 3: Right → Left (Bottom row)
    if top <= bottom:  # ✅ Check karo row valid hai ya nahi
        for i in range(right, left - 1, -1):
            ans.append(matrix[bottom][i])
        bottom -= 1  # ✅ Bottom boundary ko ek row upar le jao

    # 🔹 Step 4: Bottom → Top (Leftmost column)
    if left <= right:  # ✅ Check karo column valid hai ya nahi
        for i in range(bottom, top - 1, -1):
            ans.append(matrix[i][left])
        left += 1  # ✅ Left boundary ko ek column right le jao


print(ans)