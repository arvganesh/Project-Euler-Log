from math import factorial
def nCr(n,r):
    f = factorial
    return float(f(n) / f(r) / f(n-r))
print str(float(7 * (1 - (nCr(60,20)) / (nCr(70,20)))))[:11]
