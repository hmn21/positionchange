import pandas as pd
from datetime import datetime
import os
import glob
import csv

# date is set to today at default, and can be changed to any date, format 'YYYYMMDD'
#date = datetime.now().strftime("%Y%m%d")
date = '20160318'
# Caculate last price, total volume, and average best bid size, average best ask size, average bid ask spread for each contract in a specific date, generate SHFE_10_date.csv
path = "\\\\172.30.50.120\\nautilusdata\\SHFE_10"
os.chdir(path)
names = []
avg_BBSs = []
avg_BASs = []
avg_spreads = []
lastPrices = []
volumes = []
dirlist = os.listdir()
dirlist.sort()
for i in dirlist:
	os.chdir(path + os.sep + i)
	l = len(glob.glob('*'+date+'*.tick'))
	if l == 0:
		continue
	elif l == 1:
		tick_path = glob.glob('*'+date+'*.tick')[0]
		tick = pd.read_csv(tick_path)
	elif l == 2:
		day_path = glob.glob('*'+date+'*D.tick')[0]
		night_path = glob.glob('*'+date+'*N.tick')[0]
		day = pd.read_csv(day_path)
		night = pd.read_csv(night_path)
		tick = night.append(day, ignore_index=True)
	names.append(i)
	avg_BBS = tick['bbz1'].mean()
	avg_BAS = tick['baz1'].mean()
	avg_BASs.append(avg_BAS)
	avg_BBSs.append(avg_BBS)
	bb = tick['bb1']
	ba = tick['ba1']
	b = (bb > 0) & (bb < 9999999999)
	a = (ba > 0) & (ba < 9999999999)
	index = a & b
	spread = ba[index] - bb[index]
	avg_spread = spread.mean()
	avg_spreads.append(avg_spread)
	lastPrice = tick.lastPrice.iloc[-1]
	volume = tick.volume[tick.volume < 9999999999].sum()
	lastPrices.append(lastPrice)
	volumes.append(volume)

with open('C:\\Users\\Johnson\\Desktop\\SHFE_10_'+date+'.csv', 'w+') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
	writer.writerow(('DATE', 'CONTRACT', 'PRICE', 'VOLUME', 'Avg BBS', 'Avg BAS', 'Avg Spread'))
	for j in range(len(names)):
		writer.writerow((date, names[j], lastPrices[j], volumes[j], avg_BBSs[j], avg_BASs[j], avg_spreads[j]))

path = "\\\\172.30.50.120\\nautilusdata\\DCE"
os.chdir(path)
names = []
avg_BBSs = []
avg_BASs = []
avg_spreads = []
lastPrices = []
volumes = []
dirlist = os.listdir()
dirlist.sort()
for i in dirlist:
	os.chdir(path + os.sep + i)
	l = len(glob.glob('*'+date+'*.tick'))
	if l == 0:
		continue
	elif l == 1:
		tick_path = glob.glob('*'+date+'*.tick')[0]
		tick = pd.read_csv(tick_path)
	elif l == 2:
		day_path = glob.glob('*'+date+'*D.tick')[0]
		night_path = glob.glob('*'+date+'*N.tick')[0]
		day = pd.read_csv(day_path)
		night = pd.read_csv(night_path)
		tick = night.append(day, ignore_index=True)
	names.append(i)
	avg_BBS = tick['bbz1'].mean()
	avg_BAS = tick['baz1'].mean()
	avg_BASs.append(avg_BAS)
	avg_BBSs.append(avg_BBS)
	bb = tick['bb1']
	ba = tick['ba1']
	b = (bb > 0) & (bb < 9999999999)
	a = (ba > 0) & (ba < 9999999999)
	index = a & b
	spread = ba[index] - bb[index]
	avg_spread = spread.mean()
	avg_spreads.append(avg_spread)
	lastPrice = tick.lastPrice.iloc[-1]
	volume = tick.volume[tick.volume < 9999999999].sum()
	lastPrices.append(lastPrice)
	volumes.append(volume)

with open('C:\\Users\\Johnson\\Desktop\\DCE_'+date+'.csv', 'w+') as csvfile:
	writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
	writer.writerow(('DATE', 'CONTRACT', 'PRICE', 'VOLUME', 'Avg BBS', 'Avg BAS', 'Avg Spread'))
	for j in range(len(names)):
		writer.writerow((date, names[j], lastPrices[j], volumes[j], avg_BBSs[j], avg_BASs[j], avg_spreads[j]))