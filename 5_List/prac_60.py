def getMinDiff(arr, n, k):
        n = len(arr)
        arr.sort()
        result = arr[n-1]-arr[0]
        
        for i in range(1,n):
            if arr[i]-k <0:
                continue
            
            minh = min(arr[0]+k,arr[i]-k)
            maxh = max(arr[i-1]+k,arr[n-1]-k)
            
            result = min(result,maxh-minh)
        return result

# Example usage
k = 2
arr = [1, 5, 8, 10]
print(getMinDiff(arr, len(arr), k))  # Output: 5
