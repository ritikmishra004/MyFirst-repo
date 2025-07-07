#Hashing
'''Hashing ek technique hai jisme data ko ek fixed size value mein convert kiya jata hai (called hash).
    Iska main purpose hai fast searching and retrieval.'''

arr = [1,1,2,2,2,4,5,5,6,9,2,4,5]
number = int(input("enter any number : "))

freq = {}  # Empty dictionary to store frequency

for num in arr:            # Har element ke liye loop
    if num in freq:        # Agar num pehle se dictionary me hai
        freq[num] += 1     # Toh uska count +1 kar do
    else:
        freq[num] = 1      # Nahi hai toh 1 se start karo

# Ab check karo ki input number ka frequency > 1 hai ya nahi
if freq.get(number,0)>1:     #.get(key, default) method use karta hai. #Agar number 1 se zyada baar aaya hai, toh duplicate hai.
    print(f"{number} is a dupliacte (occurs {freq[number]})times")
else:
    print(f"{number} is not duplicate (occurs {freq.get(number,0)})")
    #Use .get() method instead of freq[number] — taaki agar key exist nahi karti ho tab bhi safe 0 return

