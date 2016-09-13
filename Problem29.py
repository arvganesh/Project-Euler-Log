distinct_powers = set() # Can't contain duplicates.
for a in xrange(2, 101):
    for b in xrange(2, 101):
        distinct_powers.add(a**b)
print len(distinct_powers) # Number Of Combinations
