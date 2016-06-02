"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a**2 + b**2 = c**2
For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc
"""
import math

a,b = 0,0
for i in range(1,10**3):
	for j in range(i+1,10**3):
		if i**2 + j**2  == (1000 - i - j)**2:
			a,b = i,j
			break
	if a > 0:
		break

print "result : "+ str(a*b*(1000-a-b))