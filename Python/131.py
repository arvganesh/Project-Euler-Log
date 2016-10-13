from Euler import is_prime
def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

ps = eraSieve(1000000)
c = 0
for x in xrange(1, 577):
    if ps[(x + 1)**3 - x**3]:
        c += 1
print c
