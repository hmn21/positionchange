from __future__ import print_function
import urllib2
import time
from datetime import datetime, timedelta
import os.path
import logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
date = datetime.today()
file_name1 = 'USDCNH_'+date.strftime('%Y%m%d')+'.csv'
file_name2 = 'USDCNY_'+date.strftime('%Y%m%d')+'.csv'
if os.path.isfile(file_name1) :
	f1 = open(file_name1, 'a')
else:
	f1 = open(file_name1, 'w+')
	print('UtcQuotetime', 'UtcRecvtime', 'Price', sep=',', file=f1)
if os.path.isfile(file_name2) :
        f2 = open(file_name2, 'a')
else:
		f2 = open(file_name2, 'w+')
		print('UtcQuotetime', 'UtcRecvtime', 'Price', sep=',', file=f2)

while 1:
	try:
		req1 = urllib2.Request('http://203.90.242.126/rn=1463101035224list=fx_susdcnh')
		resp1 = urllib2.urlopen(req1)
		s1 = resp1.read()
		req2 = urllib2.Request('http://203.90.242.126/rn=1463101035224list=fx_susdcny')
		resp2 = urllib2.urlopen(req2)
		s2 = resp2.read()
	except:
		logging.info('URLError')
		continue
	l1 = s1.split(',')
	l2 = s2.split(',')
	f3 = open('USDCNH_latest.txt', 'w+')
	f4 = open('USDCNY_latest.txt', 'w+')
	t = datetime.utcnow()
	t1 = datetime.strptime(l1[0][23:], '%H:%M:%S')
	t1 = t1 - timedelta(hours=8)
	t2 = datetime.strptime(l2[0][23:], '%H:%M:%S')
        t2 = t2 - timedelta(hours=8)
	utcRv = (t.hour * 3600 + t.minute * 60 + t.second) * 1000 + t.microsecond / 1000
	utcQt1 = (t1.hour * 3600 + t1.minute * 60 + t1.second) * 1000 + t1.microsecond / 1000
	utcQt2 = (t2.hour * 3600 + t2.minute * 60 + t2.second) * 1000 + t2.microsecond / 1000
	print(datetime.today().strftime('%Y%m%d'), l1[0][23:], l1[8], file=f3)
	print(datetime.today().strftime('%Y%m%d'), l2[0][23:], l2[8], file=f4)
	print(utcQt1, utcRv, l1[8], sep=',', file=f1)
	print(utcQt2, utcRv, l2[8], sep=',', file=f2)
	f3.close()
	f4.close()
	time.sleep(1)
	if datetime.today().day != date.day:
		logging.info('Day changed')
		f1.close()
		f2.close()
		date = datetime.today()
		file_name1 = 'USDCNH_'+date.strftime('%Y%m%d')+'.csv'
		file_name2 = 'USDCNY_'+date.strftime('%Y%m%d')+'.csv'
		if os.path.isfile(file_name1) :
			f1 = open(file_name1, 'a')
		else:
			f1 = open(file_name1, 'w+')
			print('UtcQuotetime', 'UtcRecvtime', 'Price', sep=',', file=f1)
		if os.path.isfile(file_name2) :
			f2 = open(file_name2, 'a')
		else:
			f2 = open(file_name2, 'w+')
			print('UtcQuotetime', 'UtcRecvtime', 'Price', sep=',', file=f2)
	if datetime.today().isoweekday() == 6 and datetime.now().hour == 4:
		logging.info('A week ends, program exit')