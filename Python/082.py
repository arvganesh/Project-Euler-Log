matrix = []
with open("practicefile.txt", "r") as f:
    text = f.readlines()
    for line in text:
        line = [int(i) for i in line.split()]
        matrix.append(line)

n, m = len(matrix), len(matrix[0])
cost = [matrix[i][-1] for i in xrange(n)]
for i in xrange(m-2, -1, -1):
	cost[0] += matrix[0][i]
	for j in xrange(1, n):
		cost[j] = min(cost[j], cost[j-1]) + matrix[j][i]
	for j in xrange(n-2, -1, -1):
		cost[j] = min(cost[j], cost[j+1] + matrix[j][i])
print min(cost)
