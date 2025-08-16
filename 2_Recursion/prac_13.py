# sum subsequence 

def subsequence(i, f, summ, num, arr):
    if i == len(arr):
        if summ == num:
            print(f)
        return
    
    # include current element
    f.append(arr[i])
    subsequence(i+1, f, summ + arr[i], num, arr)
    
    # exclude current element
    f.pop()
    subsequence(i+1, f, summ, num, arr)

arr = [1,2,3,4,5,6]
f = []
num = 6
subsequence(0, f, 0, num, arr)