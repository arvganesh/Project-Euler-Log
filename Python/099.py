from math import log10
count = 1
big_line = 1
my_log = 0
with open("exponent.txt","r") as f:
    text = f.readlines()
    for line in text:
        base, exp = line.split(",")
        base = int(base)
        exp = int(exp)
        logNum = exp*log10(base)
        if logNum > my_log:
            my_log, big_line = logNum, count
        count += 1
f.close()
print big_line
