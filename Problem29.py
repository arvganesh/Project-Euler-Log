distinct_powers = set()
for a in xrange(2, 101):
    for b in xrange(2, 101):
        distinct_powers.add(a**b)
print len(distinct_powers)
