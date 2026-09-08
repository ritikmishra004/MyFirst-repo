# check if a sting is palindrom or not
def palindrom(arr,i,n):
    if (i >= n//2):
        return True
    if (arr[i] != arr[n-i-1]):
        return False
    #recursive call ka result return karna zaroori hai
    return palindrom(arr,i+1,n)
    
    

arr = "madam"
n= len(arr)
print(palindrom(arr,0,n))
