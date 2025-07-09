# Find square root of the number using binary search

def floorSqrt(n):
    low = 1
    high = n

    # 🔸 Binary search karenge 1 se n ke beech
    while low <= high:
        mid = (low + high) // 2        # 🔹 Mid value nikaali
        val = mid * mid                # 🔹 Mid ka square calculate kiya

        if val <= n:
            # ✅ Agar mid^2 ≤ n, to iska matlab ye answer ho sakta hai
            # 🔹 Lekin ho sakta hai koi aur bada mid ho jiska square bhi ≤ n ho
            # 🔹 Isliye left half hata do, right half pe jao
            low = mid + 1
        else:
            # ❌ Agar mid^2 > n, to mid bada hai
            # 🔹 To right half hata do
            high = mid - 1

    # 🔸 Jab loop khatam hoga, high wo last value hoga jiska square ≤ n hai
    return high

# 🔹 Function call
n = 28
ans = floorSqrt(n)
print("The floor of square root of", n, "is:", ans)
