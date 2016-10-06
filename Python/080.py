def isRational(n):
    n = n ** 0.5
    if int(n) == n:
        return True
    return False

def irrationalList():
    lst = []
    for x in xrange(1, 101):
        if isRational(x):
            continue
        lst.append(x)
    return lst

def squareRoot(n):
    # Calculates to the nth digit without rounding.
    limit = 10 ** 101 # 100 digits. so limit = 10 ^ 100 + 1
    a = 5 * n
    b = 5
    while b < limit:
        if a >= b:
            a -= b
            b += 10
        else:
            a *= 100
            b = ((b/10) * 100 )+ 5
    return b/100

def sumOfDigits(n):
    sp = 0
    for val in n:
        val = int(val)
        sp += val
    return sp

irr = irrationalList()
s= 0
for x in irr:
    irrationalDec = str(squareRoot(x))
    s += sumOfDigits(irrationalDec)
print s
