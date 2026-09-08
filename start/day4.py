'''Given a random non-negative number, you have to return the digits of this number within 
an array in reverse order.

Example (Input => Output):
35231 => [1,3,2,5,3]
0     => [0]'''
# way 1
def reverse(digit):
        Array = []
        s = str(digit)
        rev = s[::-1]
        for i in rev:
            num = int(i)
            Array.append(num)
        return(Array)

# 2nd way
def reverse2 (digit):
        array = []
        while digit >= 1:
                array.append(digit%10)
                digit//=10
        return array

digit = 3456
print(reverse(3456))
print(reverse2(9876))
