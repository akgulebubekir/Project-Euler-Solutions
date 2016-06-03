#-*-coding:utf-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import common

primes = common.getPrimes(10**6)

numbers = "1234567"
palPrimes = []

def isPrime(num):
	global primes

	for p in primes:
		if num % p == 0:
			return False
	return True

for i in common.getPermutations(numbers):
	#performance booster
	if i[-1:] in "245678":
		continue

	elif isPrime(int(i)):
		palPrimes.append(int(i))

print "result : " + str(max(palPrimes)) 




