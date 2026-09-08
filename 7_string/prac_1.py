# 1021. Remove Outermost Parentheses

s = "(()())(())"
result = ""   # Final answer yahan banega
count = 0     # Count track karega kitne '(' abhi open hain

for ch in s:  # Har character pe loop
    if ch == '(':  # Jab '(' mile
        # Jab andar wale parentheses ho (count > 0), tabhi usko result mein daalna
        if count > 0:
            result += ch
        # Har '(' pe count badhao
        count += 1
    else:  # Jab ')' mile
        # Pehle count kam karo, kyunki ek bracket close ho raha hai
        count -= 1
        # Agar andar wale parentheses close ho rahe ho (count > 0), tabhi daalna
        if count > 0:
            result += ch

# Final result print
print(result)
