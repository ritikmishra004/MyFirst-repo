# Finding the number that appear once and others are twice
# using xor

arr = [1,1,2,3,3,4,4,5,5,6,6]

xor = 0
for num in arr:
    xor ^= num

print(xor)