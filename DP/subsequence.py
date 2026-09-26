# subsequence 
# vvip

def solve(i, arr, f):
    if i == len(arr):
        print(f)
        return  # agar ye hata do to bhi chalega, kyunki neeche kuch nahi
        # but if you write extra code yaha ke neeche, wo run ho jayega

    
    # pick (include current element)
    f.append(arr[i])
    solve(i + 1, arr, f)
    
    # backtrack (remove last element)
    f.pop()
    solve(i + 1, arr, f)


arr = [1, 2, 3]
f = []
print("All possible subsequences are:")
solve(0, arr, f)
