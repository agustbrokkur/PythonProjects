"""
Special Pythagorean triplet
Problem 9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2

For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def pythagTrip(n):
	for a in xrange(1, n / 3):
		for b in xrange(a + 1, n/2):
			c = n - a - b
			if a**2 + b**2 == c**2:
				return (a, b, c)
	return "nothing"
		


answer = pythagTrip(1000)
print answer
result = 1
for a in answer:
	result *= a
print result

for number in xrange(1001):
	temp = pythagTrip(number)
	if temp != "nothing":
		print number, ": ", pythagTrip(number)