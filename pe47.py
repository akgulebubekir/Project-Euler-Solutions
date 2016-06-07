#-*- coding:utf-8 -*-

"""
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2 × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

import common

primes = common.getPrimes(10**5)

def getPrimeFactorsFast(number):
	global primes
	primeFactors = []
	for i in primes:
		if number % i == 0 and i not in primeFactors:
			primeFactors.append(i)
		if i>number/2:
			break
	return primeFactors

def numCanditatesAround(num,isPrev=False,lim = 4):
	nc = 0
	while True and nc<=lim:
		if  isPrev:
			num -=1
		else:
			num +=1
		
		if len(getPrimeFactorsFast(num)) == 4:
			nc +=1
		else:
			break
	return nc

result = -1

for i in range(10**5,10**6,4):
	if len(getPrimeFactorsFast(i)) == 4 and numCanditatesAround(i)+numCanditatesAround(i,True) == 3:
		result = i - numCanditatesAround(i,True)
		break

print "result : "+ str(result)
