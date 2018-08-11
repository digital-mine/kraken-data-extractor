import re
import urllib 
from urllib import request
import time
from datetime import datetime, timedelta
import os

def apend(n,typee):
	g=[]
	e=0
	f=n
	for i in num:
		if e==f:
			g.append(typee(i.replace('\n','')))
			f+=4
		e+=1
	return g
def euro():
	z=0
	eur=[]
	for i in prix:
		eur.append(i*vol[z])
		z+=1
	return eur

start=time.time()
file=open('trades_.txt','r')
num=file.readlines()
file.close()
allt=[]
allt_=[]
z=0
j=2#epoca
print ('Lenght untested:',len(num))
for i in num:
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
		

prix=apend(0,float)
vol=apend(1,float)
bs=apend(3,str)
sell=[]
buy=[]
#####
for i in bs:
	if str(i)=='s':
		sell.append(i)
	if str(i)=='b':
		buy.append(i)
######		
eurr=euro()
temp=(float(num[-2].replace('\n',''))-float(num[2].replace('\n','')))
eu_vol=(float(temp)/sum(eurr))
print ('Lenght tested',len(allt_))	
file=open('new_trades_small.txt', 'w')
file.close()
file=open('new_trades_small.txt', 'a')
for i in allt_:
	file.write(i)
file.close()	
file=open('new_trades_small.txt','r')
num=file.readlines()
file.close()

one=(float(num[-4].replace('\n','')))-(float(num[0].replace('\n','')))
two=one/(float(num[0].replace('\n','')))
three=two*100
one_=float(min(prix))-float(max(prix))
two_=one_/float(max(prix))
three_=two_*100

a=float(num[2].replace('\n',''))
b= float(num[-2].replace('\n',''))
delta = b - a
print('PERIOD')
print ((delta/86400),'days')
print ((delta/604800), 'weeks')
print ((delta/2592000),'months')
print ((delta/31104000),'years')
print('_______________________')
print('First price:',prix[0])
print('Last price:',prix[-1])
print("Higher price:",max(prix))
print ("Lower price:", min(prix))
print('Volumes:', sum(eurr))
print ('Volume ratio:',eu_vol)
print ('Total sales:',len(sell))
print ('Total purchses:',len(buy))
print ('TOTAL EARNINGS:',three,'%')
print('TOTAL SPREAD:',abs(three_))
print ((three)/(delta/86400),'% per day')
print ((three)/(delta/604800),'% per week')
print ((three)/(delta/2592000),'% per month')
print ((three)/(delta/31104000),'% per year')
os.rename('new_trades_small.txt','trades_.txt')

if len(num)>=400000:
	print ("I'm writing", len(num))
	file=open('trades.txt','a')
	for i in num:
		file.write(i)
	#print (i)
	file.close()
	file=open('trades_.txt','w')
	file.close()
print (time.time()-start)

