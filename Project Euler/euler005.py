"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
from math import log, floor

def smallestMultiple(n):
	result = 1
	result *= 2 ** floor(log(n, 2))
	for i in xrange(3, n + 1, 2):
		if result % i != 0:
			result *= i ** floor(log(n, i))
	return int(result)


print smallestMultiple(20)