#-*- coding:utf-8 -*-

"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

import common

nom, denom = 1,1

for i in range(10,100):
	for j in range(10,100):
		if j%10 == 0:
			continue

		fval = float(i)/float(j) 

		if fval == float(i/10)/float(j%10) and i%10 == j/10 and  fval != float(i%10)/float(j%10):
			nom *= i
			denom *= j

if denom%nom == 0:
	print "result : " +str(denom/nom)

