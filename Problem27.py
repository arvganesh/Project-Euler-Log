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
n = 0
rangeOfPrimes = 0
lst = []
lst.append(0)
maxprimerng = 0
"""
for a in range(-1000, 1000):
    for b in range(-1000, 1001):
        isPrimeChk = isPrime(getQuadNum(n, a, b))
        if(isPrimeChk):
            n += 1
            rangeOfPrimes += 1
            if rangeOfPrimes > maxprimerng:
                #lst.pop(0)
                #lst.append(rangeOfPrimes)
                maxprimerng = rangeOfPrimes
        else:
            if (rangeOfPrimes > 40):
                print rangeOfPrimes, "a: " + str(a), "b: " + str(b)
                print "maxprimerng: " + str(maxprimerng)
            if (rangeOfPrimes == 1001):
                print "a: " + str(a), "b: " + str(b)
            rangeOfPrimes = 0
            continue

"""
while isPrime(getQuadNum(n, -1000, 2)):
    print getQuadNum(n, -1000, 2)
    n += 1
    print n
#print rangeOfPrimes
