# 796. Rotate String

s = "abcde"
goal = "cdeab"
# s ke sabhi posible rotation s+s mei hote hain "abcdeabcde"
n = len(s)
m = len(goal)

if n!=m:
    print(False)
if goal in (s+s):
    print(True)
else:
    print(False)