from math import factorial
def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

primes = eraSieve(10000000)

def isSquareFree(n):
    for x in xrange(1, n):
        if x**2 > n:
            break
        if primes[x] and n % x**2 == 0:
            return False
    return True

def nCr(n,r):
    f = factorial
    return f(n) / f(r) / f(n-r)

def pascals_triangle(rows):
    result = []
    for count in range(rows):
        row = []
        for element in range(count + 1):
            row.append(nCr(count, element))
        result.append(row)
    return result

ptri = []
distinct = set()
for row in pascals_triangle(51):
    for num in row:
        distinct.add(num)

s = 0
for num in distinct:
    if isSquareFree(num):
        s += num
print s
