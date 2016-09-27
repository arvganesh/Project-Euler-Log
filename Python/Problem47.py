def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

def getFactors(n):
    primeList = eraSieve(10000)
    lst = set()
    for i in xrange(1, len(primeList)):
        if n % i == 0 and primeList[i]:
            lst.add(i)
    return lst

for x in xrange(1000, 1000000):
    plist = getFactors(x)
    plist2 = getFactors(x+1)
    plist3 = getFactors(x+2)
    plist4 = getFactors(x+3)
    if len(plist) == 4 and len(plist2) == 4 and len(plist3) == 4  and len(plist4) == 4:
        print x
        break
