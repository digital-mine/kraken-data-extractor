from urllib import request
import urllib
import re
import time
import datetime

###
file=open('last.txt','r')#should create this file before running the program for the first time
###
num=file.read()
if num=='':
	current=0
else:
	num=num.replace('\n','')
	current=int(num)
print ('CURRENT',current)
file.close()
all=urllib.request.urlopen('https://api.kraken.com/0/public/Trades?pair=XXBTZEUR').read()
list_all=re.findall("-?\d+\.?\d*",str(all))
try:
	last=int(list_all[-1])
except Exception as e:
	exit()
file=open('last.txt','w')
file.write(str(last))
file.close()
print ('LAST',last)
price =[]
volume =[]
when= []
rbs=[]
s_b_counter=0
file=open('trades.txt','a')#change this line with the one below after the first run!
#file=open('trades_.txt','a')
while last>current:
	try:
		all=urllib.request.urlopen('https://api.kraken.com/0/public/Trades?pair=XXBTZEUR&since='+str(current)).read()
	except Exception as e:
	        print ('LINK ERROR')
	list_all=re.findall("-?\d+\.?\d*",str(all))
	list_bs=re.findall("[^\W\d_]",str(all))
	try:
		current_=list_all[-1]
		print ('NEXT CURRENT',current_)
		list_all.remove(list_all[-1])
		current=int(current_)
	except Exception as e:
		print ('ERROR', current_)
		print (all)
		current=current
		print (current,'CURRENT ERROR')
		print ('Trade list lenght ERROR', len(list_all))
	timestamp= float(current/1000000000)
	value=datetime.datetime.fromtimestamp(timestamp)
	print (current, value.strftime('%d-%m-%Y %H:%M:%S'))
	bs=[]
	for i in list_bs:
		if i=='s':
			bs.append(i)
		if i=='b':
			bs.append(i)
	try:
		bs.remove(bs[0])
		bs.remove(bs[-1])
		for i in bs[:-1]:
			rbs.append(i)
	except Exception as e:
		print ('ERROR BS')
	x=0
	p=0
	v=1
	e=2
	for i in list_all:
		if p==x:
			file.write(i+'\n')
			price.append(i)
			p+=3
		if v==x:
			file.write(i+'\n')
			volume.append(i)
			v+=3
		if e==x:
			file.write(i+'\n')
			file.write(rbs[s_b_counter]+'\n')
			when.append(i)
			e+=3
			s_b_counter+=1
			
			
		x+=1
	print ('Length PRICE',len(price))
	print ('Length VOLUME',len (volume))
	print ('Length WHEN', len (when))
	print ('Length BUY SELL', len(rbs))
	print (price[-1])
	print (volume[-1])
	print (when[-1])
	print (rbs[-1])
	time.sleep(1)
print('##################################')
print ('EXTRACTOR ENDED')
print('##################################')
file.close()
