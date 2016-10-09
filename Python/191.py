from collections import Counter
from itertools import product as p
lst = [1, 3, 0, 2, 1, 0, 0, 1]
while lst[0] < 30:
  n, t, a, b, c, d, e, f = lst
  lst = [n + 1, 2 * t + b - a, c, 2 * b - a + d, t - (a + c), e, f, t]
print lst[1]
