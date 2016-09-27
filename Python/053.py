import math
def nCr(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)

count = 0

for n in xrange(1, 101):
    for r in xrange(1, n):
        var = nCr(n, r)
        if var > 1000000:
            count += 1
print count
