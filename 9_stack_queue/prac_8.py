# check for balanced parentheses

def Stack(expression):
    st = []   # Stack banao
    for it in expression:
        if it == '(' or it == '{' or it == '[':
            st.append(it)   # Opening bracket to stack mein daal do
        else:
            if len(st) == 0:
                return False   # Agar close mila pehle hi to galat
            ch = st[-1]
            st.pop()           # Top se ek nikalo
            if (it == ')' and ch == '(') or (it == ']' and ch == '[') or (it == '}' and ch == '{'):
                continue       # Agar match ho gaya to theek hai
            else:
                return False   # Mismatch mila to galat
    return len(st) == 0        # End mein stack empty hona chahiye

print(Stack("{[()]}"))   # True
print(Stack("{[(])}"))   # False
print(Stack("((()))"))   # True
print(Stack("(()"))      # False
