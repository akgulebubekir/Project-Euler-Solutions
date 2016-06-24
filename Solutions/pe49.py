#-*- coding:utf-8 -*-
"""
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""

import common

primes = common.getPrimes(10**4)
candidates = [x for x in primes if x>10**3]

results=[]

def isPermutationOf(num1,num2):
	snum = str(num2)
	for i in str(num1):
		if not i in snum:
			return False
	return True

for i in candidates:
	if (i+3330) in primes and i+(6660) in primes and isPermutationOf(i,i+3330) and isPermutationOf(i,i+6660):
		results.append(str(i)+str(i+3330)+str(i+6660))
		

print "result : "+ str(results)