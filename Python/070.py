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

def isperm(a, b):
    a = str(a)
    b = str(b)
    return sorted(a) == sorted(b)

#print totientFunc(87109)

lst= []

for x in xrange(2, 10000000):
    phi = int(str(totientFunc(x))[:-2].strip())
    phiX = float(x) / float(phi)
    if isperm(x, phi):
        if str(phiX)[0] == '1':
            lst.append((phiX, x))
print min(lst)[1]
