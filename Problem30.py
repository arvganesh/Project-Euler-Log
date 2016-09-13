def sumOfDigPow(n):
    ans = 0
    nstr = str(n)
    for i in xrange(0, len(nstr)):
        ans += int(nstr[i])**5
    return ans

def dig5thPow():
    sum_of_pow = 0
    start = 2
    while start < 10000000:
        if sumOfDigPow(start) == start:
            sum_of_pow += start
            print start
        start += 1
    return sum_of_pow
print dig5thPow()
