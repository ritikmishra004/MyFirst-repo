# monotonic stack
# next greatest integer

def nextGreaterInteger(arr):
    nge = []  # 🔹 Stack: future ke "next greater" candidates store karega
    n = len(arr)

    # 🔁 Loop right se left (kyunki hume future ke elements ka idea chahiye)
    for i in range(n-1, -1, -1):
        current = arr[i]  # 🔹 Abhi ka element

        # 🔁 Jab tak stack non-empty hai aur top ≤ current, tab tak pop
        # 👉 Kyunki wo element current ke liye next greater ho hi nahi sakta
        while nge and nge[-1] <= current:
            nge.pop()

        # 🔹 Agar stack mein kuch bacha hai to top hi next greater hai
        next_greater = nge[-1] if nge else -1

        # 🔹 Current element ko replace karo uske next greater se
        arr[i] = next_greater

        # 🔹 Current ko stack mein push karo future ke elements ke liye candidate banane
        nge.append(current)

    return arr


arr = [4,12,5,3,1,2,5,3,1,2,4,6]
nextGreaterInteger(arr)
print(arr)