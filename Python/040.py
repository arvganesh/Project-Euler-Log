def getDecimal(n):
    deciStr = ''
    for x in xrange(1, n + 1):
        deciStr = deciStr + str(x)
    return deciStr

numStr = getDecimal(1000000)
deciNum = int(numStr[0])*int(numStr[9])*int(numStr[99])*int(numStr[999])*int(numStr[9999])*int(numStr[99999])*int(numStr[999999])
# Gets 1st, 10th, 100th, 1000th, 10000th, 100000th, and 1000000th index respectively and multiplies all of them.
print deciNum
