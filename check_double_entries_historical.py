import re
import urllib 
from urllib import request
import time
from datetime import datetime, timedelta


start=time.time()
file=open('trades.txt','r')
num=file.readlines()
file.close()

allt=[]
allt_=[]
x=400000
f=1
z=0
j=2
print (len(num))
while len(num)>0:
	partial=time.time()
	for i in num[:x]:
		if z == j:
			if i not in allt:
				allt.append(i)
				allt_.append(num[z-2])
				allt_.append(num[z-1])
				allt_.append(i)
				allt_.append(num[z+1])
				
			
			else:
				if float(i) > 10000:
					print ('DOUBLE ENTRY:',i)
			
			j+=4
		z+=1
	print (f)
	print (num[:x][0])
	print (num[:x][1])
	print (num[:x][2])
	print (num[:x][3])
	del num[:x]
	print (len(num))
	print ('NEW GROUP:',len(allt_))
	print ('ROUND TIME:'time.time()-partial)
	print('_________________')
	if len(num) <= 400000:
		x=len(num)

	f+=1
	z=0
	j=2
	allt=[]	

print ('NEW GROUP',len(allt_))	
file=open('trades.txt', 'w')
file.close()
file=open('trades.txt', 'a')
x=400000
while len(allt_)>0:
	for i in allt_[:x]:
		file.write(i)
	del allt_[:x]
	if len(allt_) <= 400000:
		x=len(allt_)
	print (len(allt_), 'to go')
#####

print ('TOTAL TIME:',time.time()-start)
