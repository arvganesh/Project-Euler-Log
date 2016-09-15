
ways = 0
target = 200
for a in xrange(target, -1, -200):
    for b in xrange(a, -1, -100):
        for c in xrange(b, -1, -50):
            for d in xrange(c, -1, -20):
                for e in xrange(d, -1, -10):
                    for f in xrange(e, -1, -5):
                        for g in xrange(f, -1, -2):
                            ways += 1
print ways
