def pentaList(n):
    data = set()
    for x in xrange(1, 10000000):
        form = x * ((3*x)-1)/2
        if form % 1 == 0:
            data.add(form)
        if len(data) == n:
            break
    return data

penList = pentaList(10000)
def isPentagonal(n):
    if n in penList:
        return True
    return False

for val in penList:
    for val2 in penList:
        if val == val2:
            continue
        valI = int(val)
        valI2 = int(val2)
        if isPentagonal(valI + valI2) and isPentagonal(abs(valI - valI2)):
            print val, val2, "sum:", valI + valI2, "dif:", abs(valI - valI2)
