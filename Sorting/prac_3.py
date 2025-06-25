arr = list(map(int, input("Enter an array : ").split()))  
n = len(arr)
for i in range(n):  # n-1 passes needed
    
    didswap = 0               # Har pass ke start mein didswap = 0, check karega kya koi swap hua ya nahi

    for j in range(n - i - 1):              # adjacent elements ko compare karta hai
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            didswap = 1               # Swap hua -> to didswap ko 1 kar do


    if didswap == 0:               # Agar poore pass mein ek bhi swap nahi hua
        break                       


    print("run")           # Har pass ke baad 'run' print hota hai (yeh batata hai kitne passes lage)

print("sorted array is : ", arr) 
