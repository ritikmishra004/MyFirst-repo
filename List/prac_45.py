# leader in an array : on their right everyone should be smaller than that number 
# brute force approach

arr = [10,22,12,4,3,0,6]
n = len(arr)
lead = []
for i in range(n):
    leader = True # using flag
    for j in range(i+1,n):
        if arr[j]>arr[i]:
            leader = False
            break
    
    if leader == True :
        lead.append(arr[i])

print(lead)