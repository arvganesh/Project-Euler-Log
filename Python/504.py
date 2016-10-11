from fractions import gcd
from math import fabs
import itertools

def SquareArea(corners):
    area = 0.0
    for i in range(4):
        j = (i + 1) % 4
        area += corners[i][0] * corners[j][1]
        area -= corners[j][0] * corners[i][1]
    area = abs(area) / 2.0
    return area

memo = {}
def lattice(p1, p2):
    pair = (p1, p2)
    if pair in memo:
        return memo[pair]
    t1, t2 = fabs(p2[0] - p1[0]), fabs(p2[1] - p1[1])
    g = gcd(t1, t2) + 1
    memo[pair] = g
    return g

def boundary(p1, p2, p3, p4):
    return (lattice(p1, p2) + lattice(p2, p3) + lattice(p3, p4) + lattice(p4, p1) - 4)


def interior(p1, p2, p3, p4):
    corners = [p1, p2, p3, p4]
    A = SquareArea(corners)
    B = boundary(p1, p2, p3, p4)
    I = A - B/2 + 1
    return I

squares = set([x**2 for x in xrange(1000)])
count = 0
count = sum(1 for a, b, c, d in itertools.product(range(1, 101), repeat=4)
            if interior((a, 0),(0, b),(-c, 0),(0, -d)) in squares)
print count
