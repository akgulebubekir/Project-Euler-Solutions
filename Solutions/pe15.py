#-*-coding: utf-8 -*-
"""
Starting in the top left corner of a 2×2 grid,
 and only being able to move to the right and down, 
 there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

def fillTable(num):
	ls = []
	row = []
	for  i in range(num):
		row.append(1)
	ls.append(row)
	for i in range(1,num):
		row=[]
		row.append(1)
		for j in range(1,num):
			row.append(ls[i-1][j]+row[j-1])
		ls.append(row)
	return ls

print "result : " + str(max(fillTable(20+1)[-1]))
