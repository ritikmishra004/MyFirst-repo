# 1614. Maximum Nesting Depth of the Parentheses
'''Given a valid parentheses string s, return the nesting depth of s.
The nesting depth is the maximum number of nested parentheses.'''
'''Input: s = "(1+(2*3)+((8)/4))+1"
Output: 3
Explanation: Digit 8 is inside of 3 nested parentheses in the string.'''

s = "(1+(2*3)+((8)/4))+1"
curr_count = 0
max_count = 0
for ch in s:
    if ch == '(':
        curr_count +=1
        max_count = max(max_count,curr_count)
    elif ch == ')':
        curr_count -= 1

print(max_count)