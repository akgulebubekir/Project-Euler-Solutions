"""
	If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
"""

ones = ["one","two","three","four","five","six","seven","eigth","nine"]
tens = ["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
decs = ["eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]

def getNums(untill):
	nums=[]
	for i in range(1,untill+1):
		num=""
		if i >= 100:
			num += ones[(i/100)%10-1]+"hundred"
			if i>100 and i%100 != 0:
				num+="and"
		if i % 100>=20:
			num += tens[(i/10)%10-2]
		if i %100>10 and i % 100<20:
			num += decs[(i%10)-1]
		elif i %10>0:
			num+=ones[(i%10)-1]
		
		if i%100==10:
			num += "ten"
		nums.append(num)

	return nums

nLetter = sum([len(x) for x in getNums(999)])
nLetter += len("onethousand")

print "result : " + str(nLetter)
