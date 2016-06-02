import math
import itertools

def getPrimes(untill):
	primes = [2,3]
	num = 3
	while num < untill:
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
	return primes

def getPrimeFactors(number):
	primes = getPrimes(number)
	primeFactors = []
	for i in primes:
		if number % i == 0:
			primeFactors.append(i)
	return primeFactors

def doesContainsNumberOnce(num):
	ns = str(num)
	for i in ns:
		if ns.count(i)>1:
			return False
	return True

def isPalindrome(num):
	sNum = str(num)
	for i in xrange(len(sNum)/2):
		if sNum[i] != sNum[-(i+1)]:
			return False
	return True

def getPrimeDivisors(number, primeList):
	retVal = []
	for i in primeList:
		if i>number:
			break
		while number % i == 0:
			retVal.append(i)
			number /=i
	return retVal

def multiplyDigits(num):
	snum = str(num)
	if "0" in snum:
		return 0
	else:
		res = 1
		for i in snum:
			res *= int(i)
		return res


def getCombinations(lst):
	combs = []
	for i in xrange(1, len(lst)+1):
	   els = [list(x) for x in itertools.combinations(lst, i)]
	   combs.extend(els)
	return combs

def unifyList(lst):
	ls=[]
	for i in lst:
		if ls.count(i)==0:
			ls.append(i)
	return ls

def getDivisors(num):
	ls=[]
	for i in xrange(1,num/2+1):
		if num %i ==0:
			ls.append(i)
	return ls

def getPermutations(lst):
	if len(lst) <= 1:
		yield lst
	else:
		for perm in getPermutations(lst[1:]):
			for i in range(len(lst)):
				yield perm[:i] + lst[0:1] + perm[i:]

def isPentagonal(num):
	dnum = (math.sqrt(24*num+1)+1)/6
	return dnum == int(dnum)

def isHexagonal(num):
	dnum = (math.sqrt(8*num+1)+1)/4
	return dnum == int(dnum)