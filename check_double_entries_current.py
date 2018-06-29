import re
import urllib 
from urllib import request
import time
from datetime import datetime, timedelta
import os

start=time.time()
file=open('trades_.txt','r')
num=file.readlines()
file.close()
allt=[]
allt_=[]
z=0
j=2
print (len(num))
for i in num:
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
		
	
print ('NEW GROUP',len(allt_))	

file=open('new_trades_small.txt', 'w')
file.close()
file=open('new_trades_small.txt', 'a')
for i in allt_:
	file.write(i)

os.remove('trades_.txt')
file.close()	
file=open('new_trades_small.txt','r')
num=file.readlines()
file.close()


one=(float(num[-3].replace('\n','')))-(float(num[0].replace('\n','')))
two=one/(float(num[0].replace('\n','')))
three=two*100

print (PRICE GAIN: three,'%')
#print ((float(num[0].replace('\n',''))*two)+(float(num[0].replace('\n',''))))
#print (float(num[-3].replace('\n','')))


a=float(num[2].replace('\n',''))
b= float(num[-1].replace('\n',''))
delta = b - a
print('PERIOD')
print ((delta/86400),'days')
print ((delta/604800), 'weeks')
print ((delta/2592000),'months')
print ((delta/31104000),'years')
print('_______________________')
print ('TOTAL EARNINGS:',three,'%')
print ((three)/(delta/86400),'% per day')
print ((three)/(delta/604800),'% per week')
print ((three)/(delta/2592000),'% per month')
print ((three)/(delta/31104000),'% per year')
os.rename('new_trades_small.txt','trades_.txt')
print (time.time()-start)
