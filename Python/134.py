def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

def getSmallestNum(p1, p2):
    prime1 = p1
    prime2 = p2
    l = len(str(prime1))
    while prime1 % prime2 != 0:
        prime1 += 10**l
    return prime1


psieve = eraSieve(1500000)
primes = [x for x in xrange(5, 1500000) if psieve[x]]
s = 0
for x in xrange(len(primes) - 1):
    if primes[x] > 1000000:
        break
    s += getSmallestNum(primes[x], primes[x + 1])
print s
