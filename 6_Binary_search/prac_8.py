# find the first and last occurence of x
# using linear search

nums = [2,4,6,8,8,8,9,11,13]
n=len(nums)
k = int(input("Enter the number: "))
first = -1
last = -1

for i in range(n):
    if nums[i]== k:
        if first == -1:
            first = i
        last = i
print(first,last)