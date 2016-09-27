def isPandigital(n): # Checks if a number n is pandigital for example. "12345" is pandigital while "12344" is not.
    stringn = str(n)
    len_of_n = len(stringn)
    for x in xrange(1, len_of_n + 1):
        stringx = str(x)
        if stringx not in stringn:
            return False
    return True

def eraSieve(n): # Prime Sieve
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve
primeList = eraSieve(10000000) # Stores prime numbers up to ten million
greatest_num = 0
for i in xrange(1, 10000000):
    if primeList[i] and isPandigital(i): # If i is prime and pandigital
        if i > greatest_num:
            greatest_num = i #
print "The greatest pandigital prime is:", greatest_num
