import math
def isConcealedSquare(n):
    strn = str(n)
    if len(strn) != 19:
        return False

    if strn[::2] != '1234567890':
        return False
    return True


upperB = int(math.ceil(math.sqrt(1929394959697989990)))
lowerB = int(math.floor(math.sqrt(1020304050607080900)))
for x in xrange(lowerB , upperB + 1):
    pow2 = x ** 2
    if isConcealedSquare(pow2):
        print x
        break
