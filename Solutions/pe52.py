#-*- coding:utf-8 -*-

"""
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""
def isPermutation(num1,num2):
	snum1 = str(num1)
	snum2 = str(num2)

	if len(snum1) != len(snum2):
		return False

	for  i in snum1:
		if i not in snum2:
			return False

	return True

result = -1
for i in range(100,10**6):
	if len(str(i)) != len(str(6*i)):
		continue

	if isPermutation(i,2*i) and isPermutation(i,3*i) and isPermutation(i,4*i) and isPermutation(i,5*i) and isPermutation(i,6*i):
		result = i
		break

print "result : "+ str(result)