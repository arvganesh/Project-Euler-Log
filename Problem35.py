import itertools
def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

def perms(n):
    permList = [''.join(p) for p in itertools.permutations(str(n))]
    return permList

primeList = eraSieve(1000000)

def rotate(l,n):
    p = str(l)
    return int(p[n:] + p[:n])

my_num  = 0
def isCircularPrime(n):
    for r in xrange(len(str(n))):
        my_num = int(rotate(n, r)) # Gets Rotations
        if not primeList[my_num]:
            return False
    return True

print isCircularPrime(31)
amount = 0
for i in xrange (1, 1000000):
    if primeList[i]:
        if isCircularPrime(i):
            amount += 1
print amount
