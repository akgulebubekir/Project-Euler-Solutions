#-*-coding:utf-8 -*-

"""
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
import math

maxP, maxPsol = 0,0
for p in range(3,1001):
	solutions=[]

	for i in range(1,p/2):
		for j in range(1,i):

			if i + j > p:
				break

			if i**2 + j**2 == (p-i-j)**2:
				solutions.append((i,j,p-i-j))


	if len(solutions)> maxPsol:
		maxPsol = len(solutions)
		maxP = p

print "result : "+ str(maxP) 

