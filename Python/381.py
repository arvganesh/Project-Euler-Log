from math import factorial
from Euler import prime_sieve

def reciprocal_mod(x, m):
	assert m > 0 and 0 <= x < m
	y = x
	x = m
	a = 0
	b = 1
	while y != 0:
		a, b = b, a - x // y * b
		x, y = y, x % y
	if x == 1:
		return a % m
	else:
		raise ValueError("Reciprocal does not exist")

var = 0
def s(p):
	# (p-5)! + (p-4)! + (p-3)! + (p-2)! + (p-1)!
	# = (p-5)! * (1 + (p-4) + (p-4)(p-3) + (p-4)(p-3)(p-2) + (p-4)(p-3)(p-2)(p-1))
	# = (p-5)! * (1 + (-4) + (-4)(-3) + (-4)(-3)(-2) + (-4)(-3)(-2)(-1))
	# = (p-5)! * (1 + -4 + 12 + -24 + 24)
	# = (p-5)! * 9
	# = (p-1)! / ((p-1)(p-2)(p-3)(p-4)) * 9
	# = (p-1)! / ((-1)(-2)(-3)(-4)) * 9
	# = (p-1)! / 24 * 9
	# = (p-1)! * (3 * 3) / (3 * 8)
	# = (p-1)! * 3 / 8
	# = -1 * 3 / 8  (by Wilson's theorem)
	# = -3/8 mod p.
	# Every part of the equation is modulo a prime p > 4
	return (p - 3) * reciprocal_mod(8 % p, p) % p

psieve = prime_sieve(10 ** 8)
for x in psieve:
    if x >= 5:
        var += s(x)
print var
