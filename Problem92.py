def sumOfDigSquare(n):
    sn = str(n)
    if len(sn) == 1:
        return n ** 2
    my_sum = 0
    for val in sn:
        valInt = int(val)
        my_sum += valInt ** 2
    return my_sum

count = 0
for x in xrange(1, 10000000):
    num = sumOfDigSquare(x) # 32
    if num == 89:
        count += 1
        continue
    while True:
        var = sumOfDigSquare(num) # 13
        num = var
        if var == 89:
            count += 1
            break
        if var == 1:
            break
print count
