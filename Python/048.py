def selfPowers(n):
    my_sum = 0
    for x in xrange(1, n + 1):
        my_power = x ** x
        my_sum += my_power
    return my_sum

strPower = str(selfPowers(1000))
print strPower[(len(strPower) - 10):]
