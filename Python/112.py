def isLeftToRight(n):
    c = 0
    previous = 0
    n = str(n)
    for val in n:
        val = int(val)
        if c > 0:
            if not val >= previous:
                return False
        previous = val
        c += 1
    return True

def isRightToLeft(n):
    c = 0
    previous = 0
    n = str(n)
    for val in n:
        val = int(val)
        if c > 0:
            if not val <= previous:
                return False
        previous = val
        c += 1
    return True

def isBouncy(n):
    if isLeftToRight(n) or isRightToLeft(n):
        return False
    return True

t = 0
x = 0
ratio = 0
while True:
    if isBouncy(x):
        t += 1
        ratio = float(t) / float(x)
    if ratio == 0.99:
        print x
        break
    x += 1
