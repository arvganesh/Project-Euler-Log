def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

plist = eraSieve(1000000)
def getConsecPrimes(n):
    lst = []
    for x in xrange(2, n):
        if plist[x]:
            lst.append(x)
    return lst
clist = getConsecPrimes(1000000)
def isSumOfCP(n):
    my_sum = 0
    count = 0
    lst = []
    for x in xrange(len(clist)):
        my_sum = 0
        count = 0
        for y in xrange(x, len(clist)):
            my_sum += clist[y]
            count += 1
            if my_sum == n:
                return count
            if my_sum > n:
                break
    return False

c = 0
bigx = 0
for x in clist:
    cpNum = isSumOfCP(x)
    if cpNum > c:
        c = cpNum
        bigx = x
print "ans", bigx
