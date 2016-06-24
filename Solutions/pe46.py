#-*- coding:utf-8 -*-

"""
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1**2
15 = 7 + 2×2**2
21 = 3 + 2×3**2
25 = 7 + 2×3**2
27 = 19 + 2×2**2
33 = 31 + 2×1**2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math
import common

primes = common.getPrimes(10**4)

result = -1
for i in range(5,10**4,2):
	if i in primes:
		continue
	isGoldbach = False
	for j in range(1,i/2):
		if (i - 2 * j**2) in primes:
			isGoldbach = True
			break

	if not isGoldbach:
		result = i
		break

print "result : "+ str(result)

