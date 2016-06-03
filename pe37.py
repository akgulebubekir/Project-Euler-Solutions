#-*-coding:utf-8 -*-

"""
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right,
 and remain prime at each stage: 3797, 797, 97, and 7.
  Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

import common

primes = common.getPrimes(10**6)

#don't seek if prime has even digit or 5
optiPrimes= [x for x in primes if not any(d in str(x) for d in ["0","2","4","5","6","8"])]

tprimes = []

for p in optiPrimes:
	s = str(p)
	isTruncatable = True
	for i in range(1,len(s)):
		if not int(s[:i]) in primes or not int(s[i:]) in primes:
			isTruncatable = False
			break

	if isTruncatable:
		tprimes.append(p)

print "result : "+ str(sum(tprimes))

