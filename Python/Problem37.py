def eraSieve(n): # Prime Sieve
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

primeList = eraSieve(1000000) # Generates a list of one million booleans. All of the primes are true, and the rest are false. Based on the eratosthenes sieve.

def isTruncatablePrime(n):
    nstring = str(n)
    length = len(nstring)
    for x in xrange(length):
        my_num = int(nstring[x:]) # Starting from the beginning of a number
        other_num = int(nstring[:x + 1]) # Starting from the end of a number
        bool1 = primeList[my_num]
        bool2 = primeList[other_num]
        if not bool1 or not bool2: # If both of them are not prime, or if one of them is not prime.
            return False
    return True

count = 0
amount = 0
for x in xrange(10, 1000000):
    if primeList[x]:
        if isTruncatablePrime(x):
            print "Each Reversable Truncatable Prime is:", x
            amount += x
            count += 1 # 11 primes that are truncatable from right to left and vice versa.
        if count == 11: # Stop when count is 11.
            break
print "The sum of all reversable Truncatable numbers is:", amount
