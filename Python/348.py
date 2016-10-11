from collections import Counter
from Euler import pal_list
def isPal(n):
    return str(n) == str(n)[::-1]

cache = {}
for a in xrange(1, 100000):
    for b in xrange(1, 100000):
        x = a ** 2 + b ** 3
        if not isPal(x):
            continue
        if x not in cache:
            cache[x] = 1
        else:
            cache[x] += 1
        if cache[x] == 4:
            print x
for key, value in cache.iteritems():
    if cache[key]  > 3:
        print key, value
