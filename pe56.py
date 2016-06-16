#-*- coding:utf-8 -*-

"""
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

maxSum = 0


for a in range(1,100):
	for b in range(1,100):
		dsum = sum([int(x) for x in str(a**b)])
		if dsum> maxSum:
			maxSum = dsum

print "result : " + str(maxSum)
