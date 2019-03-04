"""
Summation of primes
Problem 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

from math import floor, sqrt

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

def sumOfPrimes(n):
	listi = [2]
	for i in xrange(1, n, 2):
		if isPrime(i):
			listi.append(i)
	return listi


primes = sumOfPrimes(1000)
primes = [1, 9, 36, 100, 225, 441, 784]
other = []
for i in xrange(1, len(primes)):
	other.append(primes[i] - primes[i - 1])

print primes
print other

next = []
while len(other) > 2:
	for i in xrange(1, len(other)):
		next.append(abs(other[i] - other[i - 1]))
	print next
	other, next = next, []

 





