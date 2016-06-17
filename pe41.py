#-*-coding:utf-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import common
import math

primes = common.getPrimes(10**6)

numbers = "1234567"
palPrimes = []

def isPrime(num):
	global primes
	for i in primes:
		if i> math.sqrt(num)+1:
			return True
		if num % i == 0:
			return False


for i in common.getPermutations(numbers):
	#performance booster
	if i[-1:] in "245678":
		continue

	elif isPrime(int(i)):
		palPrimes.append(int(i))

print "result : " + str(max(palPrimes)) 
