from Euler import prime_sieve
n, r, s = 20000000, 15000000, 0
for p in prime_sieve(n):
    x = p
    while x <= n:
        s += p * (n//x - r//x - (n - r)//x) # Floor Division, exponenet number.
        x *= p # Increasing the exponent.
print s
