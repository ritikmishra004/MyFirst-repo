# monotonic stack
# next greatest integer

def nextGreaterInteger(arr):
    nge = []  # 🔹 Stack to store potential next greater elements
    n = len(arr)

    # 🔁 Traverse from right to left
    for i in range(n-1, -1, -1):
        current = arr[i]

        # 🔁 Remove all elements <= current from stack
        while nge and nge[-1] <= current:
            nge.pop()

        # 🔹 Stack ka top hi next greater hai agar stack non-empty ho
        next_greater = nge[-1] if nge else -1

        # 🔹 Replace current element with next greater
        arr[i] = next_greater

        # 🔹 Push current element to stack (ab future ke liye candidate ban gaya)
        nge.append(current)

    return arr


arr = [4,12,5,3,1,2,5,3,1,2,4,6]
nextGreaterInteger(arr)
print(arr)