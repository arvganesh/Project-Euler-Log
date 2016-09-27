def reverseSum(n):
    strn = int(str(n)[::-1])
    return n + strn

def eachDigOdd(n):
    strn = str(n)
    for val in strn:
        vali = int(val)
        if vali % 2 == 0:
            return False
    return True

count = 0
for x in xrange(1, 1000000000):
    rsum = reverseSum(x)
    if eachDigOdd(rsum) and x % 10 != 0:
        count += 1
print count
