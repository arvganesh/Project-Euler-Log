from Euler import miller_rabin as mr

squares = set()
#2*n^2 - 1 = x
for x in xrange(2, 50000001):
    squares.add(x**2)




lst = []
c = 0
for x in xrange(2, 50000001):
    if (((pow(x, 2, 10)*2) - 1) % 10) % 2 == 0:
        continue
    if (((pow(x, 2, 100)*2) - 1) % 100) % 4 == 0:
        continue
    if (((pow(x, 2, 1000)*2) - 1) % 1000) % 8 == 0:
        continue
    if (((pow(x, 2, 10)*2) - 1) % 10) == 0 or (((pow(x, 2, 10)*2) - 1) % 10) == 5:
        continue
    if 2*(x ** 2) - 1 in squares:
        continue
    if mr(2*(x** 2) - 1):
        c += 1
print c
