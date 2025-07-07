# count of a number

num = int(input("Enter any number"))
count = 0

while num>0:
    num = int(num/10)
    count += 1
print("count",count)