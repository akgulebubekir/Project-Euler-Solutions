#-*-coding:utf-8 -*-

"""
The decimal number, 585 = 1001001001base2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

import common

numbers = [x for x in range(1,10**6) if common.isPalindrome(x) and common.isPalindrome(bin(x)[2:])]

print "result : " + str(sum(numbers))