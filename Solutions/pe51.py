#-*- coding:utf-8 -*-
"""
By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
 yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
"""

import common

primes = common.getPrimes(10**6)
primeset = set([x for x in primes if x>10**5])

patternList={}


for i in range(5,8):
	patternList[i] =[]

for p in common.getPermutations("1110000"):
	for j in range(5,8):
		if p[j-1] == "0" and "1" in p[:j] and p[:j] not in patternList[j]:
			patternList[j].append(p[:j])


def numPrimesByPattern(num,pattern):
	nump = 0
	snum = str(num)
	l = len(snum)

	for n in range(1,10):
		tnum = num
		for i in range(l):
			if pattern[i] == "1":
				tnum -= (int(snum[i])-n)*10**(l-i-1)

		if tnum in primeset:
			nump += 1

		if n > nump+3:
			break

	return nump



result = -1

for p in primeset:

	l =len(str(p))
	for pattern in patternList[l]:
		if numPrimesByPattern(p,pattern) == 8 : 
			result = p
			for i in range(l):
				if pattern[i] =="1":
					result -= (int(str(p)[i])-1)*10**(l-i-1)
			break
	
	if result>0:
		break


print "result : " + str(result)

