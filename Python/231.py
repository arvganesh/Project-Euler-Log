from Euler import prime_sieve
n, r, s = 20000000, 15000000, 0
for p in prime_sieve(n):
    j = 1
    while p ** j <= n:
        s += p * (n//p**j - r//p**j - (n - r)//p**j) # Floor Division, exponenet number.
        j += 1 # Increasing the exponent.
print s
