def repeat(number,arr):
    count = 0
    for i in range (0,n):
        if (arr[i] == number):
            count += 1 
        
    return count


arr = [2,3,4,1,1,2,5,6,1,2,1,3]
n = len(arr)
number = int(input("Enter any numer :"))
print(repeat(number,arr))