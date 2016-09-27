from Euler import is_perm


data = {}

def isPerm(a, b):
    stra = sorted(str(a))
    strb = sorted(str(b))
    return stra == strb
for a in xrange(1, 10000):
    data[a] = a ** 3

count = 0
lst = set()

for x in xrange(1, 10000):
    count = 0
    for y in xrange(1, 10000):
        dx = data[x]
        dy = data[y]
        if isPerm(dx, dy):
            count += 1
            lst.add(dx)
        if count == 5:
            print dx, dy
            break
