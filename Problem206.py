import math
def isConcealedSquare(n):
    strn = str(n)
    if len(strn) != 19:
        return False

    if strn[0] != '1' or strn[2] != '2' or strn[4] != '3' or strn[6] != '4' or strn[8] != '5' or strn[10] != '6' or strn[12] != '7' or strn[14] != '8' or strn[16] != '9' or strn[18] != '0':
        return False
    return True


upperB = int(math.ceil(math.sqrt(1929394959697989990)))
lowerB = int(math.floor(math.sqrt(1020304050607080900)))
for x in xrange(lowerB , upperB + 1):
    pow2 = x ** 2
    if isConcealedSquare(pow2):
        print x
        break
