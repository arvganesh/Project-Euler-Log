def digitContain(a,b):
    if sorted(str(a)) != sorted(str(b)):
        return False
    return True

x = 2
while x > 1:
    two = 2*x
    three = 3*x
    four = 4*x
    five = 5*x
    six = 6*x
    if digitContain(x, two) and digitContain(x, three) and digitContain(x, four) and digitContain(x, five) and digitContain(x, six):
        print x
        break
    x += 1
