# finding the nth root of an integer using linear search

def nth_root(n, m):
    # x^n = m
    for x in range(1, m+1):  # 1 se m tak saare values try karenge
        power = x ** n       # x^n calculate karo

        if power == m:
            return x         # ✅ Exact root mil gaya
        elif power > m:
            break            # ❌ x bada ho gaya, ab koi aur value kaam nahi karegi

    return -1  # Agar koi integer root nahi mila

# Example:
n = 3
m = 27

print(f"The {n}th root of {m} is:", nth_root(n, m))
