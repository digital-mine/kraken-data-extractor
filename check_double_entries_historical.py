import re
import urllib 
from urllib import request
import time
from datetime import datetime, timedelta


start=time.time()
file=open('new_trades.txt','r')
num=file.readlines()
file.close()

allt=[]
allt_=[]
x=300000
y=0
f=1
z=0
j=2
print (len(num))
while len(num)>0:
	partial=time.time()
	for i in num[y:x]:
		if z == j:
			if i not in allt:
				allt.append(i)
				allt_.append(num[z-2])
				allt_.append(num[z-1])
				allt_.append(i)
			
			else:
				if float(i) > 10000:
					print ('DOUBLE ENTRY:',i)
			
			j+=3
		z+=1
	print (f)
	print (num[:x][0])
	print (num[:x][1])
	print (num[:x][2])
	del num[:x]
	print (len(num))
	print ('NEW GROUP',len(allt_))
	print ('ROUND TIME':time.time()-partial)
	print('_________________')
	if len(num) <= 300000:
		x=len(num)

	f+=1
	z=0
	j=2
	allt=[]
	
	
print ('NEW GROUP',len(allt_))	
file=open('new_trades.txt', 'w')
file.close()
file=open('new_trades.txt', 'a')
x=300000
while len(allt_)>0:
	for i in allt_[:x]:
		file.write(i)
	del allt_[:x]
	if len(allt_) <= 300000:
		x=len(allt_)
	print (len(allt_), 'to go')
#####

print ('TOTAL TIME:',time.time()-start)
