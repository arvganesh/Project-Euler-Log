import random
def m_r(n):
    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    for repeat in range(20):
        a = 0
        while a == 0:
            a = random.randrange(n)
        if not miller_rabin_pass(a, s, d, n):
            return False
    return True

def miller_rabin_pass(a, s, d, n):
    a_to_power = pow(a, d, n)
    if a_to_power == 1:
        return True
    for i in range(s-1):
        if a_to_power == n - 1:
            return True
        a_to_power = (a_to_power * a_to_power) % n
    return a_to_power == n - 1

def diagonalNum(): # n is the number of row
    increment = 2
    getDiaNum = 1
    #limit = (n-1)/2
    sideLen = 1.0
    c = 0.0
    while True:
        count = 1
        while count <= 4:
            getDiaNum += increment
            if m_r(getDiaNum):
                c += 1
            count += 1
        increment += 2
        sideLen += 4
        if c / sideLen < 0.10:
            return increment - 1 # Gets row amount.

print diagonalNum()
