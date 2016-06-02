"""
1 Jan 1900 was a Monday.
Thirty days has September,April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
months = {1:31 ,2:28 ,3:31 ,4:30 ,5:31 ,6:30 ,7:31 ,8:31 ,9:30 ,10:31 ,11:30 ,12:31}


numFirstSundays = 0
passedDay = -1
day = "monday"
for year in range(1901,2001):
	for m in months:
		numMonth = months[m]
		if m == 2 and year % 4 == 0:
			print "leap year: " + str(year)
			numMonth+=1
		if days[passedDay%7] == "sunday":
			print "y:" +str(year) + " m:"+str(m)+" d:"+str(passedDay)
			numFirstSundays+=1
		for d in range(numMonth):
			passedDay+=1

print "result : "+ str(numFirstSundays)
