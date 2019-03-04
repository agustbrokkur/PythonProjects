"""
Largest palindrome product
Problem 4

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
import time
def largestPalindrome(n, m):
	largest = 0
	for i in xrange(n, m):
		for j in xrange(n, i):
			k = i * j
			if k > largest and k == int(str(k)[::-1]):
				largest = k
	return largest


def largestPalindromeFaster(n, m):
	largest = 0
	for i in xrange(m - 1, n - 1, -1):
		for j in xrange(i, n - 1, -1):
			k = i * j
			if k < largest:
				break
			if k > largest and k == int(str(k)[::-1]):
				largest = k
	return largest


start = time.time()
print largestPalindrome(100, 1000)
end = time.time()
print(end - start)

start = time.time()
print largestPalindromeFaster(100, 1000)
end = time.time()
print(end - start)
