import collections
def getTriangular(n):
    triangleList = []
    for i in xrange(1, n + 1):
        formula = i*(i+1)/2
        triangleList.append(formula)
    return triangleList
def getPentagonal(n):
    pentaList = []
    for i in xrange(1, n + 1):
        formula = i*(3*i - 1)/2
        pentaList.append(formula)
    return pentaList

def getHexagonal(n):
    hexList = []
    for i in xrange(1, n + 1):
        formula = i*(2*i - 1)
        hexList.append(formula)
    return hexList


tri = getTriangular(100000)
penta = getPentagonal(100000)
hexa = getHexagonal(100000)

tri_multiset = collections.Counter(tri)
penta_multiset = collections.Counter(penta)
hexa_multiset = collections.Counter(hexa)

overlap = list((hexa_multiset & penta_multiset & tri_multiset).elements())

print overlap
