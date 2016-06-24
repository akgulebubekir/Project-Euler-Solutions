#-*- coding:utf-8 -*-

"""
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 299 altogether! If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)
"""

a = open("pe67_triangle.txt").read().splitlines()

def recSumAtRow(rowData, rowNum):
    for i in range(len(rowData[rowNum])):
        rowData[rowNum][i] += max([rowData[rowNum+1][i],rowData[rowNum+1][i+1]])
    if len(rowData[rowNum])==1: return rowData[rowNum][0]
    else: return recSumAtRow(rowData, rowNum-1)

ls=[]
for i in a:
	row = []
	for j in i.split():
		row.append(int(j))
	ls.append(row)

print "result : "+ str( recSumAtRow(ls, len(ls)-2))