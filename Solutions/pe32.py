#-*- coding:utf-8 -*-

"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

"""

def isPalindromeCandidate(num):
	ns = str(num)
	for i in ns:
		if ns.count(i)>1:
			return False
	return True


pPairs= []

for i in range(1,10**3):

	if "0" in str(i) or not isPalindromeCandidate(i):
		continue

	for j in range(1,10 ** 4):

		if "0" in str(j) or not isPalindromeCandidate(j):
			continue

		snum = str(i) + str(j) + str(i*j)

		if not len(snum) == 9 or  "0" in snum or not isPalindromeCandidate(snum):
			continue

		elif i*j not in pPairs:
			pPairs.append(i*j)

print "Result: "+ str(sum(pPairs))