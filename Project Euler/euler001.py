"""
Problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
from math import floor

def problem001(n=1000, a=3, b=5):
	result = 0
	for i in xrange(n):
		if i % a == 0 or i % b == 0:
			result += i
	return result

def easy001(n=1000, a=3, b=5):
	n -= 1
	c = a * b
	result = sumSeries(a, n) + sumSeries(b, n) - sumSeries(c, n)
	return result
	

def sumSeries(x, y):
	a = floor(y / x)
	a *= a + 1
	result = (a / 2) * x
	return result

print problem001()
print easy001(100000000000000000)