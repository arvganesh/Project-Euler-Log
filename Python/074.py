from math import factorial
def facSum(n):
    sn = str(n)
    sumfac = 0
    for val in sn:
        valInt = int(val)
        sumfac += factorial(valInt)
    return sumfac


def getChainLength(x):
    facSet = set()
    n = x
    facSet.add(x)
    while True:
        fac = facSum(n)
        if fac in facSet:
            break
        facSet.add(fac)
        n = fac
    return len(facSet)

c = 0
for x in xrange(1, 1000001):
    if getChainLength(x) == 60:
        c += 1
print c
