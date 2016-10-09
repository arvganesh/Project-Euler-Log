from Euler import prime_sieve
def divisors(n):
    # get factors and their counts
    factors = {}
    nn = n
    i = 2
    while i*i <= nn:
        while nn % i == 0:
            if not i in factors:
                factors[i] = 0
            factors[i] += 1
            nn //= i
        i += 1
    if nn > 1:
        factors[nn] = 1

    primes = list(factors.keys())
    def generate(k):
        if k == len(primes):
            yield 1
        else:
            rest = generate(k+1)
            prime = primes[k]
            for factor in rest:
                prime_to_i = 1
                for _ in range(factors[prime] + 1):
                    yield factor * prime_to_i
                    prime_to_i *= prime
    for factor in generate(0):
        yield factor
def eraSieve(n):
    sieve=[True]*(n+1)
    sieve[:2] = [False, False]
    sqrt = int(n**.5)+1
    for x in xrange(2, sqrt):
        if sieve[x]:
            sieve[2*x::x]=[False]*(n/x-1)
    return sieve

primes = eraSieve(100000)
def rad(n):
    m = 1
    for d in divisors(n):
        if primes[d]:
            m *= d
    return m

s = 0
dictionary = {}
for x in xrange(1, 100001):
    dictionary[x] = rad(x)

dictionary  = [v[0] for v in sorted(dictionary.items(), key=lambda(k,v): (v,k), reverse=False)]

print dictionary[9999]
