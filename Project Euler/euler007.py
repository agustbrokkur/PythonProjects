"""
10001st prime
Problem 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

from math import floor, sqrt
import time

# Mine
def numberedPrime(n):
	listi = [2, 3, 5, 7]
	limit = 180000
	primes = [i for i in xrange(3, limit, 2) if i % 3 != 0 and i % 5 != 0 and i % 7 != 0]
	i = 0
	while len(listi) < n:
		x = primes[i]
		listi.append(x)
		for p in primes:
			if p % x == 0 and p != x:
				primes.remove(p)
		i += 1
	return listi[-1]

# Project Euler helper function
def isPrime(n):
	if n == 1:
		return False
	if n < 4:
		return True
	if n % 2 == 0:
		return False
	if n < 9:
		return True
	if n % 3 == 0:
		return False
	else:
		r = floor(sqrt(n))
		f = 5
		while f <= r:
			if n % f == 0:
				return False
			if n % (f + 2) == 0:
				return False
			f = f+6
	return True

# Project Euler answer function
def givenPrimes(limit):
	count = 1
	candidate = 1
	while count != limit:
		candidate += 2
		if isPrime(candidate):
			count += 1
	return candidate

start = time.time()
print numberedPrime(10001)
end = time.time()
print "\nTime taken is: ", (end - start)

start = time.time()
print givenPrimes(10001)
end = time.time()
print "\nTime taken is: ", (end - start)