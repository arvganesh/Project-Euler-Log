from Euler import is_prime
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
s = 0

def test(n):
    for factor in divisors(n):
        if not is_prime(factor + (n / factor)):
            return False
    return True

for x in xrange(1, 10 ** 8):
    if test(x):
        s += x
print s
