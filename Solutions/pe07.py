#-*- coding: utf-8 -*-

"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?

"""
import math

primes = [2,3]
num = 3
while len(primes)<10001:
	num += 2
	flag = True
	for i in primes:
		if i> math.sqrt(num)+1:
			break
		if num % i == 0:
			flag = False
			break
	if flag:
		primes.append(num)

print "result : " + str(primes[-1])

