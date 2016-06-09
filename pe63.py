#-*-coding:utf-8 -*-

"""
The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
"""

candidates=[]

for digit in range(1,10):
	for p in range(1,50):
		if len(str(digit**p)) == p:
			candidates.append((digit,p))

print "result : "+ str(len(candidates))

