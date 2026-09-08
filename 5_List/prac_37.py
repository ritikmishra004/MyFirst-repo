# majority Element greator than n/2 using hashing

arr = [2,2,3,2,2,4,2,2,3,2,3,4,5,2,5]
n= len(arr)

hash_map ={}

for num in arr:
    if num in hash_map:
        hash_map[num] += 1
    else:
        hash_map[num] = 1
# we can use this for checking the count:
# for num in arr:
#     hash_map[num]=hash_map.get(num,0)+1

for num,count in hash_map.items():
    if count > n//2:
        print(num,count)
        break
else:
    print("no")