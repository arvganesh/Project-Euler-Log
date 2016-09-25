from Euler import prime_sieve
lst = set() # Used for no duplicates.
psieve = prime_sieve(10000)
for c in psieve[:85]:
    for b in psieve[:369]:
        for a in psieve[:7072]:
            q=a*a+b**3+c**4
            if q >= 50000000: break
            lst.add(q)
print len(lst)
