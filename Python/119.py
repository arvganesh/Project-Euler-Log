from math import log10
def sumOfDigits(x):
    s = 0
    for val in str(x):
        s += int(val)
    return s

def findPows(x):
    lst = []
    for y in range(2,x):
        for z in range(2,10):
            lst.append(y**z)
    lst.remove(4)
    lst.remove(8)
    lst.remove(9)
    lst = list(set(lst))
    lst.sort()
    return lst

fp = findPows(100)

count = 0
for val in fp:
    x = 1
    num = sumOfDigits(val)
    if num != 1:
        while x < val:
            x *= num
    if x == val:
        count += 1
        print x, count
    else:
        continue
    if count == 30:
        break    
