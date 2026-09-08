# finding missing numbers
# using hashing

arr =[2,5,3,1]

hash_set = set(arr)

for i in range(1,max(arr)+1):
    if i not in hash_set:
        print("missing number :",i)