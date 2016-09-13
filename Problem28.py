def diagonalNum(n):
    increment = 2
    getDiaNum = 1
    sumOfNums = 0
    count = 1
    limit = (n-1)/2
    for i in xrange(1, limit + 1):
        while count <= 4:
            getDiaNum += increment
            sumOfNums += getDiaNum
            count += 1             
        increment += 2
        count = 1
    return sumOfNums + 1

print diagonalNum(1001)
