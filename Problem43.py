from itertools import permutations
permList = [''.join(p) for p in permutations(str("1234567890"))] # Similar to '.split()' in java
def divis(n):
    s = str(n)
    if len(s) == 10:
        if int(s[1:4]) % 2 == 0:
            if int(s[2:5]) % 3 == 0:
                if int(s[3:6]) % 5 == 0:
                    if int(s[4:7]) % 7 == 0:
                        if int(s[5:8]) % 11 == 0:
                            if int(s[6:9]) % 13 == 0:
                                if int(s[7:10]) % 17 == 0:
                                    return True
    return False

s = 0
for p in permList:
    if divis(p):
        s += int(p)
print s
