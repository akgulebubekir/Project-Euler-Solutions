#-*- coding: utf-8 -*-

"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

def digitFactorial(num):
	res  = 0
	for i in str(num):
		res += math.factorial(int(i))

	return res

result = sum([x for x in range(3,10**5) if x == digitFactorial(x)])

print "result : "+ str(result)


