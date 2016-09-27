import math

resultmax = 0
result = 0
for p in xrange(2, 1001, 2):
    resultnum = 0
    p3 = int(p / 3)
    for a in xrange(1, p):
        if (p*(p - 2*a)) % (2*(p-a)) == 0: # Derived In Comments.
            resultnum += 1
    if resultnum > resultmax:
        resultmax = resultnum
        result = p
print result

"""
We have two rules.
a^2 + b^2 = c^2
a + b + c = p

We can then right the second equation, in terms of c.
This becomes. c = p - a - b

Then we substitute c into the 1st equation and we get:
a^2 + b^2 = (p - a - b)^2, which is equal to a^2 + b^2 = p^2 + a^2 + b^2 -2pa – 2pb + 2ab

Then when we isolate b on the left side, we get
b = (p^2 - 2pa) / (2p-2a)

The equation on line 9 is just the factored form of the equation above.
"""
