"""
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

import math
import common

num = 600851475143

primes = common.getPrimes(math.sqrt(num))

primeFactors = [p for p in primes if num % p == 0]

print "result : " + str(max(primeFactors))

