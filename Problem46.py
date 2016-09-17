def eraSieve(n): # Prime Sieve
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

primes = eraSieve(1000000)
primeList = [p for p, i in enumerate(primes) if primes[p]]

def isOddC(n):
    if n % 2 == 0:
        return False
    if primes[n]:
        return False
    return True

lim = 1000
results = set()
for p in primeList[:1000]:
    for i in xrange(lim):
        result = p + 2*i**2
        if result < 1000000:
            if isOddC(result):
                results.add(result)

for x in xrange(3, 1000000, 2):
    if isOddC(x):
        if x not in results:
            print x
            break
