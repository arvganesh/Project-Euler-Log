import math
def getQuadNum(n, a, b):
    return n**2 + a*n + b
def isPrime(n):
    if n > 0:
        sqrtN = int (math.sqrt(n))
    else:
        sqrtN = n
    ceil_of_n = math.ceil(sqrtN)
    if (n % 2 == 0):
        return False
    for i in xrange(2, int(ceil_of_n)):
        if (n % i == 0):
            return False
    return True

nMax = 0
aMax = 0
bMax = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        n = 0
        while isPrime(math.fabs(getQuadNum(n, a, b))):
            n += 1
        if n > nMax:
            nMax = n
            aMax = a
            bMax = b


print "n: " + str(nMax) + " a: " + str(aMax) + " b: " + str(bMax) + " ans: " + str(aMax*bMax)
