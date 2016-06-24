#-*-coding: utf-8 -*-

"""
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import common

primes = set(common.getPrimes(10**6))

circularPrimes = [2,3,5]

for i in primes:

	if sum([int(d) for d in str(i)]) % 3  == 0:
		continue

	if len([d for d in str(i) if int(d)%2 == 0 or int(d)%5 == 0]) > 0:
		continue

	isCircular = True
	s = str(i)
	for j in range(0,len(s)):
		if not int(s[j:]+s[:j]) in primes:
			isCircular = False
			break

	if isCircular:
		circularPrimes.append(i)

print "result : " + str(len(circularPrimes))
