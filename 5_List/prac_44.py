# Next permutation

arr = [2, 3, 4, 2, 5, 0, 2, 0]
n = len(arr)

# step 1 : Dip index dhoondo - jahan arr[i] < arr[i+1] ho right se
# is index se hi next permutation banana possible hota hai
# example: [2,3,4,2,5,0,2,0] → index = 4 (kyunki 0 < 2)

index = -1
for i in range(n - 2, -1, -1):   # n-2 se 0 tak jaayenge, kyunki 0 bhi valid dip ho sakta hai
    if arr[i] < arr[i + 1]:
        index = i
        break   # pehla dip milte hi ruk jao, wahi important hai

# key point:
# agar dip index nahi mila, iska matlab array already last (largest) permutation hai
# to humein ise ascending order mein (smallest permutation) convert karna hoga

if index == -1:
    arr.reverse()  # poora array reverse kar do (last → first permutation)
else:
# step 2 : ab right side se aisa number dhoondo jo dip se thoda bada ho
# usko swap karo dip index ke element ke sath
    for i in range(n - 1, index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break

    # step 3 : dip ke baad wali subarray ko reverse karo
    # taaki smallest lexicographical arrangement mile
    arr[index + 1:] = reversed(arr[index + 1:])

print(arr)