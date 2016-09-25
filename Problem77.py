def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

plist = eraSieve(1000000)

def getSolutions(n):
    choices = (p for p in xrange(1, n + 1) if plist[p])
    possible=[1]+[0]*n
    for i in choices:
        for j in range(i, n + 1):
            possible[j]+=possible[j-i]
    return possible[n]


choices = (p for p in xrange(1, 1000000 + 1) if plist[p])
for x in choices:
    if getSolutions(x) > 5000:
        break
print x
