from fractions import Fraction
def rootConverge(a):
    c = 0
    d = 2
    n = 3
    for x in xrange(2, a):
        n, d = n + d*2, n + d
        if len(str(n)) > len(str(d)): c += 1
    return  c

print rootConverge(1000)
