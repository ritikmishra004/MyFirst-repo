# for only one answer

def subsequence(i, f, summ, num, arr):
    if i == len(arr):
        if summ == num:
            print(f)
            return True
        else: return False
    
    # include
    f.append(arr[i])
    if subsequence(i+1, f, summ + arr[i], num, arr) == True:
        return True
    f.pop()
    
    # exclude
    if subsequence(i+1, f, summ, num, arr) == True:
        return True
    
    else: return False


arr = [1,2,3,4,5,6]
f = []
num = 6
subsequence(0, f, 0, num, arr)
