#-*- coding:utf-8 -*-
"""
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053).
 In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
"""

cubes = {}

for i  in range(1,10**4):
	cubes[i] = ''.join(sorted(str(i**3)))

cvals = cubes.values()
candidates = set([x for x in cvals if cvals.count(x) == 5])


result = min([x for x in cubes if cubes[x] in candidates])


print "result : "+ str(result)