def isPandigital(n): # Checks if a number n is pandigital for example. "12345" is pandigital while "12344" is not.
    stringn = str(n)
    len_of_n = len(stringn)
    for x in xrange(1, len_of_n + 1):
        stringx = str(x)
        if stringx not in stringn:
            return False
    return True
def multiPan(a, b): # Checks if the a,b and the product(combined) are a pandigital number
    multiplier = a*b
    product = str(multiplier)
    stra = str(a)
    strb = str(b)
    total = stra + strb + product # Adds up everything. For example, 12 * 34 = 56789 would become 123456789
    if isPandigital(total) and len(total) == 9: # Checks if its a pandigital from 1 through 9
        return True
    return False

pandigitalSet = set() # Doesn't allow duplicates.
for a in xrange(2000, 1, -1):
    for b in xrange(2000, 1, -1):
        multi = a*b
        if multiPan(a, b):
            multi = a*b
            pandigitalSet.add(multi) # Adds the product of a and b to the set.
print sum(pandigitalSet) # Prints sum of the set.
