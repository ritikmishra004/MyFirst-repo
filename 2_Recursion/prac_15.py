# for count of sequence
def subsequence(i, summ, num, arr):
    if i == len(arr):
        return 1 if summ == num else 0   # agar sum mila to 1 count otherwise 0
    
    # include current element
    left = subsequence(i+1, summ + arr[i], num, arr)
    
    # exclude current element
    right = subsequence(i+1, summ, num, arr)
    
    return left + right


arr = [1,2,3,4,5,6]
num = 6
count = subsequence(0, 0, num, arr)
print("Total subsequences:", count)
