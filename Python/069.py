def prime_factors(n):
        """Returns all the prime factors of a positive integer"""
        factors = set()
        d = 2
        while n > 1:
            while n % d == 0:
                factors.add(d)
                n /= d
            d = d + 1
            if d*d > n:
                if n > 1: factors.add(n)
                break
        return factors
def totientFunc(n):
    pf = prime_factors(n)
    s = 1.0
    for val in pf:
        val = float(val)
        s = s * float((1 - (1 / val)))
    return s * n

bigx = 0
bignum = 0
for x in xrange(1, 1000001):
    phi = totientFunc(x)
    num = float(x / phi)
    if num > bignum:
        bignum = num
        bigx = x
print bigx
