#-*- coding: utf-8 -*-

"""
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
import common

allDivisors=[]
primes= common.getPrimes(21)

for i in range(1,21):
	pdivs = common.getPrimeDivisors(i,primes)
	for p in pdivs:
		if not p in allDivisors or allDivisors.count(p) < pdivs.count(p):
			allDivisors.append(p)

mult = 1
for i in allDivisors:
	mult *= i

print "result : " + str(mult)
