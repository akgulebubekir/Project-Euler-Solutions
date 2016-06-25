import os
import time

#common.py runner
import sys
sys.path.append("Solutions")


numSolved = 40

for  i in range(1,numSolved+1):
	filename ="Solutions/pe"+str(i).zfill(2)+".py"
	if not os.path.exists(filename):
		continue
	start = time.time()
	execfile(filename,{})
	print("Problem "+ str(i) +" : "+ str(time.time()-start) )
