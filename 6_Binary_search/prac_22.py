# Minimum Number of Days to Make m Bouquets
# Brute force

def possible(bloomday,day,m,k):
    n = len(bloomday)
    count = 0
    no_of_bouquet = 0
    for bloom in bloomday:
        if bloom<=day:
            count+=1
        else:
            no_of_bouquet += count//k
            count = 0
    no_of_bouquet += count//k
    if no_of_bouquet >= m:
        return True
    else:
        return False

def bouquets(bloomday,m,k):
    for i in range(min(bloomday),max(bloomday)+1):
        if possible(bloomday,i,m,k) == True:
            return i
bloomday = [7,7,7,7,12,7,7]
m = 2 # number of bouquets
k = 3 # number of different flower in one bouquet
print(bouquets(bloomday,m,k))