"""
Sum square difference
Problem 6

The sum of the squares of the first ten natural numbers is,
1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers 
and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def sumSquareDif(n):
	sumOfSquares = (n * (n + 1) * ((2 * n) + 1)) / 6
	squareOfSum = ((n * (n + 1)) / 2)**2
	return squareOfSum - sumOfSquares

print sumSquareDif(100)

"""
How to find sum of the cubes
0	1	8	27	64	125
  1	  7   19  37  61
    6   12  18  24
	  6    6   6


An^4 + Bn^3 + Cn^2 + Dn

A + B + C + D = 1

16A + 8B + 4C + 2D = 9

81A + 27B + 9C + 3D = 36

256A + 64B + 16C + 4D = 100

625A + 125B + 25C + 5D = 225


16A + 8B + 4C + 2D = 9
-2A - 2B - 2C - 2D = -2
14A + 6B + 2C 	   = 7

81A + 27B + 9C + 3D = 36
-3A - 3C  - 3C - 3D = -3
78A + 24B + 6C      = 33

256A + 64B + 16C + 4D = 100
-4A    -4B   -4C - 4D = -4
252A + 60B + 12C      = 96

625A + 125B + 25C + 5D = 225
 -5A    -5B   -5C - 5D = -5
620A + 120B + 20C      = 220

78A + 24B + 6C = 33
-42A - 18B - 6C = -21
36A + 6B = 12

252A + 60B + 12C = 96
-84A - 36B - 12C = -42
168A + 24B = 54

168A + 24B = 54
-144A - 24B = -48
24A = 6
A = 6/24 = 1/4

36(1/4) + 6B = 12
9 + 6B = 12
6B = 12 - 9
6B = 3
B = 3/6 = 1/2

14A + 6B + 2C = 7
14(1/4) + 6(1/2) + 2C = 7
14/4 + 3 + 2C = 7
2C = 7 - 14/4 - 3
2C = 28 - 14 - 12
2C = 2/4 = 1/2
C = 2/2 = 1

78A + 24B + 6C = 33
78(1/4) + 24(1/2) + 6C = 33
39/2 + 24/2 + 6C = 33
6C = 33 - 39/2 - 24/2
6C = 66 - 39 - 24 / 2
6C = 3 / 2
C = 3/(2 *6)
C = 1/4

1/4 + 1/2 + 1/4 + D = 1
D = 0

An^4 + Bn^3 + Cn^2 + Dn
(1/4)n^4 + (1/2)n^3 + (1/4)n^2
(1/4)n^2 * (n^2 + 2n + 1)
(1/4)n^2 * ((n^2 + n) + (n + 1))
(1/4)n^2 * (n(n + 1) + (n + 1))
(1/4)n^2 * (n + 1) * (n + 1)

n^2 * (n + 1) * (n + 1)
-----------------------
          4
"""