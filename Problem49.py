import itertools
def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

def isPerm(a,b):
    stra = str(a)
    strb = str(b)
    if sorted(stra) != sorted(strb):
        return False
    return True

def primePerms(n):
    permList = [''.join(p) for p in itertools.permutations(str(n))]
    primeList = eraSieve(10000)
    lst = []
    x = 0
    while x < len(permList):
        my_num = permList[x]
        if primeList[int(my_num)]:
            lst.append(int(my_num))
        x += 1

    return sorted(lst)
    print primePerms(1487)

def getFourDigPrimes():
    fourDig = []
    primeList = eraSieve(10000)
    fourDig = [x for x in xrange(1001, 10000, 2) if primeList[x]]
    return fourDig

fourDigPrimes = getFourDigPrimes()

fourDigSet = set(fourDigPrimes)

length = len(fourDigPrimes)

for a in xrange(length-1):
    for b in xrange(a+1, length-1):
        p1 = fourDigPrimes[a]
        p2 = fourDigPrimes[b]
        if isPerm(p1, p2):
            val = p2 + (p2 - p1)
            if val in fourDigSet and isPerm(p1, val):
                # If the next term in the sequence is a four digit prime, and is also a permutation of the 1st number.
                print '%s%s%s' % (str(p1), str(p2), str(val)) # Print out the sorted values.
                
