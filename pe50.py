#-*- coding:utf-8 -*-

"""
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""
import common
import math

primes = common.getPrimes(10**6)
primeset = set(common.getPrimes(10**6))

result, resCount = 0, 0

for i in range(0,len(primes)):
	num = 0
	count = 0
	for j in primes[i:]:
		count+=1
		num +=j 

		if num < 10**6 and num in primeset and resCount<count:
			resCount = count
			result = num
		if num>10**6:
			break

print "result : "+ str(result)
