"""
Largest prime factor
Problem 3

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

from math import sqrt

def largestFactor(n):
	prime = 2
	listi = []
	if n % prime == 0:
		listi.append(prime)
		while n % prime == 0:
			n /= 2
	prime += 1
	while prime <= sqrt(n):
		if n % prime == 0:
			listi.append(prime)
			while n % prime == 0:
				n /= prime
		prime += 2
	if n not in listi and n != 1:
		listi.append(n)
	return listi



print largestFactor(10**10)
lista = [1, 3, 4]