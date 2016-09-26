romanData = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))
def convert(romanNum):
    for val in romanNum:
        if val not in "IVXLCDM":
            return 0
    # We now know that the number is a roman numeral.
    num = 0
    for nums in romanNum:
        rd = romanData[nums]
        num += rd # Gets the value of numbers, and adds. Might be wrong. For example, "IV" would become 6. For any subtractive pair, you would subtract 2, 20, or 200. 6 - 2 = 4.
    # Check for subtractive pairs. Only one is allowed per number.
    if "IV" in romanNum or "IX" in romanNum:
        num -= 2
    if "XL" in romanNum or "XC" in romanNum:
        num -= 20
    if "CD" in romanNum or "CM" in romanNum:
        num -= 200
    return num


def toRomanNumeral(n, convertedString):
    if n == 0:
        return convertedString
    for row in xrange(13):
        num = romanNumeralMap[row][1]
        letter = romanNumeralMap[row][0]
        if num > n:
            continue
        convertedString += letter
        n = n - num
        return toRomanNumeral(n, convertedString)

def isMinimal(numeral):
    return numeral == toRomanNumeral(convert(numeral), '')

charSaved = 0
with open("roman89.txt","r") as f:
    text = f.readlines()
    for line in text:
        line = line.rstrip('\n')
        romanNum = convert(line)
        if isMinimal(line):
            continue
        if len(line) == len(toRomanNumeral(romanNum, '')):
            continue
        if line == toRomanNumeral(romanNum, ''):
            continue
        #print line, toRomanNumeral(romanNum, ''), len(line) - len(toRomanNumeral(romanNum, '')), count
        charSaved += len(line) - len(toRomanNumeral(romanNum, ''))
f.close()
print "The number of characters saved is:", charSaved
