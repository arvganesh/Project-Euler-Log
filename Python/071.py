N = 3/7.
L = 1000000
mina = N
for b in range(L, L-7, -1):
    a = N - int(b*N) * 1.0/b
    if mina > a != 0: mina, minD = a,b

print int(minD*N), "/", minD
