from urllib import request
import urllib
import re
import time
import datetime

current=0
file=open('last.txt','r')
all=urllib.request.urlopen('https://api.kraken.com/0/public/Trades?pair=XXBTZEUR').read()
list_all=re.findall("-?\d+\.?\d*",str(all))
last=int(list_all[-1])
print (last)
file.write(last)
file.close()
price =[]
volume =[]
when= []
file=open('trades.txt','a')
while last>current:
	try:
		all=urllib.request.urlopen('https://api.kraken.com/0/public/Trades?pair=XXBTZEUR&since='+str(current)).read()
	except Exception as e:
	        print ('ERRORE LINK')
	list_all=re.findall("-?\d+\.?\d*",str(all))
	try:
		current_=list_all[-1]
		print ('CURRENT',current_)
		list_all.remove(list_all[-1])
		current=int(current_)
	except Exception as e:
		print ('ERROR', current_)
		print (all)
		current=current
		print (current,'ERROR CURRENT')
		print ('Length list trade ERROR', len(list_all))
	timestamp= float(current/1000000000)
	value=datetime.datetime.fromtimestamp(timestamp)
	print (current, value.strftime('%d-%m-%Y %H:%M:%S'))
	x=0
	p=0
	v=1
	e=2
	for i in list_all:
		if p==x:
			price.append(i)
			file.write(i+'\n')
			p+=3
		if v==x:
			file.write(i+'\n')
			volume.append(i)
			v+=3
		if e==x:
			file.write(i+'\n')
			when.append(i)
			e+=3
		x+=1
	print ('Length PRICE',len(price))
	print ('Length VOLUME',len (volume))
	print ('Length WHEN', len (when))
	print (price[-1])
	print (volume[-1])
	print (when[-1])
	time.sleep(1)
  
file.close()
