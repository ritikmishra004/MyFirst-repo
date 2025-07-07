#Parameterized


def sum_n(i,total):
    if i < 1:
        print ("sum is", total)
        return
    sum_n(i-1,total+i)

x = int(input("enter any number"))
sum_n(x,0)