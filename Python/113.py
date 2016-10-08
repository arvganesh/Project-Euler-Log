import math
def Choose(n,r):
    f = math.factorial
    return f(n) / f(r) / f(n-r)


print Choose(100 + 10, 10) + Choose(100 +9, 9) - 10 * 100 - 2
