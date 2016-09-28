from fractions import Fraction
result = 0
count  = 4
value2 = []
value2.append(Fraction(1))
for i in xrange(1,101):
    if i ==2:
        value2.append(Fraction(i))
    else:
        if (i - 2) % 3 == 0:
            value2.append(Fraction(count))
            count = Fraction(count + 2)
        else:
            value2.append(Fraction(1))
for i in xrange(1,101):
    value = Fraction(1/value2[i])
    j = 1
    while i != j:
        value = Fraction(value + value2[i-j])
        value = Fraction (1/value)
        j = j + 1
    value = Fraction (value + 2)
    strValue = str(value)
    if i == 99:
        strValue100S = str(value).split('/')
        strNum100 = strValue100S[0]
        for k in strNum100:
            result = result + int(k)
print(result)
