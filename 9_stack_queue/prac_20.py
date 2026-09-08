# Trapping Rain Water - Two Pointer Approach (O(n) Time, O(1) Space)

def trapping_water(arr):
    n = len(arr)
    Lmax = 0   # 🔹 Left max height so far
    Rmax = 0   # 🔹 Right max height so far
    total = 0  # 🔹 Total trapped water
    l = 0      # 🔹 Left pointer
    r = n - 1  # 🔹 Right pointer
    
    # 🔄 Jab tak left pointer right pointer ke andar hai tab tak loop chalega
    while l < r:
        
        # Agar left side ka height chhota ya barabar hai right side ke height se
        if arr[l] <= arr[r]:
            # Agar Lmax bada hai current height se, to yahan water trap hoga
            if Lmax > arr[l]:
                total += Lmax - arr[l]
            else:
                # Agar current height zyada hai to Lmax update kar do
                Lmax = arr[l]
            l += 1  # Left pointer ko aage badhao
        
        # Agar right side ka height chhota hai
        else:
            # Agar Rmax bada hai current height se, to yahan water trap hoga
            if Rmax > arr[r]:
                total += Rmax - arr[r]
            else:
                # Agar current height zyada hai to Rmax update kar do
                Rmax = arr[r]
            r -= 1  # Right pointer ko peeche le jao
    
    return total

# Example
arr = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trapping_water(arr))  # Output: 6


"""
💡 Key Points (Hinglish):

1. Hum do pointer (l aur r) ka use karte hain left aur right se start karke.
2. Lmax & Rmax variables store karte hain ab tak ka maximum height left aur right se.
3. Agar left side ka height chhota ya equal hai right side se:
    - Agar Lmax bada hai current height se → water trap hota hai.
    - Nahi to Lmax ko update karte hain.
4. Agar right side ka height chhota hai:
    - Agar Rmax bada hai current height se → water trap hota hai.
    - Nahi to Rmax ko update karte hain.
5. Har step par hum pointer ko move karte hain jis side ka height chhota hota hai.
6. Ye approach O(n) time me aur O(1) extra space me kaam karti hai.
"""
