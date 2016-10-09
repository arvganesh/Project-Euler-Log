from math import fabs
def getRectangles(m, n):
    return ((m*(m + 1)) / 2)*((n*(n + 1)) / 2)
    
area = 0
mn = 1000
for m in xrange(1, 1000):
    for n in xrange(1, 1000):
        rect = getRectangles(m, n)
        num = fabs(rect - 2000000)
        if num < mn:
            mn = num
            area = m * n
            bign = n
            bigm = m
print area
