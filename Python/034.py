import math
def sumOfDigFac(n):
    stringn = str(n)
    sumoffac = 0
    for i in xrange(0, len(stringn)):
        sumoffac += math.factorial(int(stringn[i]))
    if sumoffac != n:
        return False
    return True

i = 3
my_sum = 0
while i < 1000000:
    if sumOfDigFac(i):
        my_sum += i
    i += 1
print my_sum
