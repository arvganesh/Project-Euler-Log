def parse():
    matrix = []
    c = 0
    with open("matrix.txt", "r") as f:
        text = f.readlines()
        for line in text:
            line = line.strip()
            matrix.append((line.split(",")))
    return matrix

matrix = parse()
for a in xrange(80):
    matrix[a] = [int(i) for i in matrix[a]]


def minimum(a, b):
    if a < b:
        return int(a)
    return int(b)

for x in xrange(78, -1, -1):
    matrix[79][x] += matrix[79][x + 1]
    matrix[x][79] += matrix[x + 1][79]

for a in xrange(78, -1, -1):
    for b in xrange(78, -1, -1):
        matrix[a][b] += minimum(matrix[a + 1][b], matrix[a][b + 1])


print matrix[0][0]
