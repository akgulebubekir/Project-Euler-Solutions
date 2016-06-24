#-*- coding: utf-8 -*-
"""
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
"""

numIters={}

for i in range(2,10**6):
	s = i
	chain = []
	isCalculated = False
	while s!=1:
		if s in numIters:
			isCalculated=True
			numIters[i] = numIters[s]+len(chain)
			break
		if(s%2) == 0:
			s/=2
		else:
			s= 3*s+1
		chain.append(s)
	if not isCalculated:
		numIters[i] = len(chain)+1

result  = max(numIters, key=numIters.get)

print "result : "+ str(result)
