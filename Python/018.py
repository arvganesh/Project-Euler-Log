pyramid = []
with open("practicefile.txt", "r") as f:
    text = f.readlines()
    for line in text:
        line = [int(i) for i in line.split()]
        pyramid.append(line)

def solve(pyr):
    while len(pyr) > 1:
        above = pyr[len(pyr) - 2]
        below = pyr[len(pyr) - 1]
        for x in xrange(len(above)):
            above[x] += max(below[x], below[x + 1])
        pyr.pop()
    return pyr[0][0]

print solve(pyramid)
