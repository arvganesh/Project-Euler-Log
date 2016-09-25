from math import log10
s = 0
for x in xrange(1, 10):
    s += int(1 / (1 - log10(x)))
print s
