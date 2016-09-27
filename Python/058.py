import random
def m_r(n):
    """
    Check n for primalty:  Example:

    >miller_rabin(162259276829213363391578010288127)    #Mersenne prime #11
    True

    Algorithm & Python source:

http://en.literateprograms.org/Miller-Rabin_primality_test_(Python)

    """
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

def diagonalNum(n): # n is the number of row
    increment = 2
    getDiaNum = 1
    limit = (n-1)/2
    sideLen = 1.0
    c = 0.0
    for i in xrange(1, limit + 1):
        count = 1
        while count <= 4:
            getDiaNum += increment
            if m_r(getDiaNum):
                c += 1
            count += 1
        increment += 2
        sideLen += 4
    return c / sideLen

#print diagonalNum(7)

for x in xrange(26230, 100000):
    ratio = diagonalNum(x)
    if ratio < 0.10:
        break
print x
