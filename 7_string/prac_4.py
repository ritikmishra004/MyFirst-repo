# Largest Odd Number in String

num = "35427"

for i in range(len(num)-1,-1,-1):
    if int(num[i])%2 == 1:
        print(num[:i+1])
        break
else:
    print("")

# the second way 
for i in range(len(num)-1,-1,-1):
    if num[i] in '13579':
        print(num[:i+1])
        break
else:
    print("")