#-*- coding:utf-8 -*-

"""
Euler discovered the remarkable quadratic formula:

n**2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

The incredible formula  n**2 − 79n + 1601 was discovered, which produces 80 primes for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n**2 + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

"""
import common

primes = common.getPrimes(10**4)

coeff,lenChain = 0, 0 
for  a in range(-10**3,10**3):
	for b in range(-10**3,10**3):
		n = 1
		while (n**2 + a*n + b) in primes:
			n+=1

		if lenChain<n:
			lenChain = n
			coeff = a*b

print "result : "+ str(coeff)
