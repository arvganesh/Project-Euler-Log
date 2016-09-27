from collections import Counter

lst = []
countA = Counter()
for a in xrange(1, 5):
    for b in xrange(1, 5):
        for c in xrange(1, 5):
            for d in xrange(1, 5):
                for e in xrange(1, 5):
                    for f in xrange(1, 5):
                        for g in xrange(1, 5):
                            for h in xrange(1, 5):
                                for i in xrange(1, 5):
                                    probSum = a + b + c + d + e + f + g + h + i
                                    countA[probSum] += 1
lowerB = 9
upperB = 36
size = 4 ** 9
probDataP = {}
for x in xrange(lowerB, upperB+1):
    occur = countA[x]
    probability = float(occur) / float(size)
    probDataP[x] = probability


countB = Counter()
for a2 in xrange(1, 7):
    for b2 in xrange(1, 7):
        for c2 in xrange(1, 7):
            for d2 in xrange(1, 7):
                for e2 in xrange(1, 7):
                    for f2 in xrange(1, 7):
                        probSum2 = a2 + b2 + c2 + d2 + e2 + f2
                        countB[probSum2] += 1

lowerB2 = 6
upperB2 = 36
size2 = 6 ** 6
probDataC = {}
for y in xrange(lowerB2, upperB2+1):
    occur2 = countB[y]
    probability2 = float(occur2) / float(size2)
    probDataC[y] = probability2

# We want the probability that P wins over C

totalProb = 0.0
for peteSum in xrange(lowerB, upperB+1):
    peteProb = probDataP[peteSum] # Getting Probs of all numbers from lower b to upper b
    for colinSum in xrange(lowerB2, peteSum): # colinSum has to be less than pete sum for us to calculate the probability of pete winning.
        colinProb = probDataC[colinSum] # Getting Probs of all numbers in colin's lower b to upper b
        totalProb += peteProb * colinProb

print totalProb
