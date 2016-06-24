#-*- coding:utf-8 -*-

"""
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
"""

import sys
sys.setrecursionlimit(1500)

numsStr={}

def rec(num, itr):
	if itr == 0:
		return (1,num)
	else:
		res = rec(num,itr-1)
		return (res[1],num*res[1]+res[0])


numResult = 0

for i in range(1,10**3):
	res = rec(2,i)
	if len(str(res[0]+res[1]))>len(str(res[1])):
		numResult +=1

print "result : "+ str(numResult)