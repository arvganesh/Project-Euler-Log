target = 100
ns = range(1, target)
ways = [1] + [0]*target
print ways
for n in ns:
    for i in range(n, target+1):
        ways[i] += ways[i-n]
print "Ways to make change =", ways[target]
