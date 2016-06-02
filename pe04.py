#-*- coding: utf-8 -*-

"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import common

ls= []
for i in range(101,999):
	for j in range(101,999):
		if common.isPalindrome(i*j):
			ls.append(i*j)

print "result : "+ str(max(ls))
