# Rearrange Array Elements by Sign in alternative sign
# if the positive and negative are not equal

arr = [1, -2, 3, -4, 3, 2, -6, -9, 5, 7, -8, -10, 11, 13, 14]
n = len(arr)
positive, negative = [], []

# Separate positive and negative
for i in range(n):
    if arr[i] < 0:
        negative.append(arr[i])
    else:
        positive.append(arr[i])

# Fill alternately
if len(positive) < len(negative):
    for i in range(len(positive)):
        arr[2*i] = positive[i]
        arr[2*i+1] = negative[i]
    index = len(positive) * 2
    for i in range(len(positive), len(negative)):
        arr[index] = negative[i]
        index += 1
else:
    for i in range(len(negative)):
        arr[2*i] = positive[i]
        arr[2*i+1] = negative[i]
    index = len(negative) * 2
    for i in range(len(negative), len(positive)):
        arr[index] = positive[i]
        index += 1

print(arr)
