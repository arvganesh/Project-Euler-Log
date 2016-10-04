from Euler import is_palindromic
import math
limit = 10 ** 8
sqrtL = int(math.ceil(limit ** 0.5))
num = 0
ssum = 0
my_list = []
for i in xrange(1, sqrtL + 1):
    num = i * i
    for x in xrange(i + 1, sqrtL + 1):
        num += x * x
        if num > limit: break
        if is_palindromic(num) and num not in my_list:
            ssum += num
            my_list.append(num)
print ssum
