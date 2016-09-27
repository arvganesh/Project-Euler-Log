def getSum(dig):
    str_d = str(dig)
    if dig == 1:
        return 1
    if dig % 10 and str_d[0] == 1:
        return 1
    my_sum = 0
    for val in str_d:
        valInt = int(val)
        my_sum += valInt
    return my_sum

nums = 0
for a in xrange(2, 100):
    for b in xrange(2, 100):
        digSum = getSum(a**b)
        if digSum > nums:
            nums = digSum
print nums
