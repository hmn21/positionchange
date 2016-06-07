from __future__ import print_function
import paramiko
from datetime import datetime, timedelta
import functools
import os
import pandas as pd

class AllowAnythingPolicy(paramiko.MissingHostKeyPolicy):
    def missing_host_key(self, client, hostname, key):
        return


hostname = "220.248.84.82"
password = "Nautilus2016"
username = "databak"
port = 209
client = paramiko.SSHClient()
client.set_missing_host_key_policy(AllowAnythingPolicy())
client.connect(hostname, port=port, username=username, password=password)
sftp = client.open_sftp()
sftp.chdir('/databak/all/EsunnyData/run')

date = (datetime.now()- timedelta(1)).strftime("%Y%m%d")
#date = "20160603"

def my_callback(filename, bytes_so_far, bytes_total):
    print('Transfer of %r is at %d/%d bytes (%.1f%%)' % (
        filename, bytes_so_far, bytes_total, 100. * bytes_so_far / bytes_total))

for filename in sorted(sftp.listdir()):
    if filename.startswith(date+'_08'):
        callback_for_filename = functools.partial(my_callback, filename)
        sftp.get(filename, filename, callback=callback_for_filename)
        day = filename
    if filename.startswith(date+'_20'):
        callback_for_filename = functools.partial(my_callback, filename)
        sftp.get(filename, filename, callback=callback_for_filename)
        night = filename


df = pd.read_csv(day, header=None)
df.columns = ['exchange', 'variety', 'utcReceiveTime', 'lastPrice', 'volume', ' volumeAcc', 'openInterest', 'bbz10', 'bbz9', 'bbz8', 'bbz7', 'bbz6', 'bbz5', 'bbz4', 'bbz3', 'bbz2', 'bbz1', 'bb10', 'bb9', 'bb8', 'bb7', 'bb6', 'bb5', 'bb4', 'bb3', 'bb2', 'bb1', 'ba1', 'ba2', 'ba3', 'ba4', 'ba5', 'ba6', 'ba7', 'ba8', 'ba9', 'ba10', 'baz1', 'baz2', 'baz3', 'baz4', 'baz5', 'baz6', 'baz7', 'baz8', 'baz9', 'baz10', 'utcQuoteTime']
l = list(df.variety.unique())
data = list()
for i in l:
    data.append(df[df.variety == i])
for i in range(len(data)):
    data[i] = data[i].drop(['exchange', 'variety'], axis=1)
    data[i] = data[i].assign(a1 = data[i].bbz1)
    data[i] = data[i].assign(a2 = data[i].bb1)
    data[i] = data[i].assign(a3 = data[i].ba1)
    data[i] = data[i].assign(a4 = data[i].baz1)
    data[i] = data[i][['utcReceiveTime', 'lastPrice', 'volume', ' volumeAcc', 'openInterest', 'a1', 'a2', 'a3', 'a4', 'bbz10', 'bbz9', 'bbz8', 'bbz7', 'bbz6', 'bbz5', 'bbz4', 'bbz3', 'bbz2', 'bbz1', 'bb10', 'bb9', 'bb8', 'bb7', 'bb6', 'bb5', 'bb4', 'bb3', 'bb2', 'bb1', 'ba1', 'ba2', 'ba3', 'ba4', 'ba5', 'ba6', 'ba7', 'ba8', 'ba9', 'ba10', 'baz1', 'baz2', 'baz3', 'baz4', 'baz5', 'baz6', 'baz7', 'baz8', 'baz9', 'baz10', 'utcQuoteTime']]
    data[i].columns = ['utcReceiveTime', 'lastPrice', 'volume', ' volumeAcc', 'openInterest', 'bbz1', 'bb1', 'ba1', 'baz1', 'bbz10', 'bbz9', 'bbz8', 'bbz7', 'bbz6', 'bbz5', 'bbz4', 'bbz3', 'bbz2', 'bbz1', 'bb10', 'bb9', 'bb8', 'bb7', 'bb6', 'bb5', 'bb4', 'bb3', 'bb2', 'bb1', 'ba1', 'ba2', 'ba3', 'ba4', 'ba5', 'ba6', 'ba7', 'ba8', 'ba9', 'ba10', 'baz1', 'baz2', 'baz3', 'baz4', 'baz5', 'baz6', 'baz7', 'baz8', 'baz9', 'baz10', 'utcQuoteTime']
for i in range(len(l)):
	dirname = '\\\\172.30.50.120\\temp\\CME_COMEX\\' + l[i]
	if not os.path.isdir(dirname):
		os.mkdir(dirname)
	filename = dirname + "\\" + l[i] + '-' + date +'-D.tick'
	data[i].to_csv(filename, index=False)

df = pd.read_csv(night, header=None)
df.columns = ['exchange', 'variety', 'utcReceiveTime', 'lastPrice', 'volume', ' volumeAcc', 'openInterest', 'bbz10', 'bbz9', 'bbz8', 'bbz7', 'bbz6', 'bbz5', 'bbz4', 'bbz3', 'bbz2', 'bbz1', 'bb10', 'bb9', 'bb8', 'bb7', 'bb6', 'bb5', 'bb4', 'bb3', 'bb2', 'bb1', 'ba1', 'ba2', 'ba3', 'ba4', 'ba5', 'ba6', 'ba7', 'ba8', 'ba9', 'ba10', 'baz1', 'baz2', 'baz3', 'baz4', 'baz5', 'baz6', 'baz7', 'baz8', 'baz9', 'baz10', 'utcQuoteTime']
l = list(df.variety.unique())
data = list()
for i in l:
    data.append(df[df.variety == i])
for i in range(len(data)):
    data[i] = data[i].drop(['exchange', 'variety'], axis=1)
    data[i] = data[i].assign(a1 = data[i].bbz1)
    data[i] = data[i].assign(a2 = data[i].bb1)
    data[i] = data[i].assign(a3 = data[i].ba1)
    data[i] = data[i].assign(a4 = data[i].baz1)
    data[i] = data[i][['utcReceiveTime', 'lastPrice', 'volume', ' volumeAcc', 'openInterest', 'a1', 'a2', 'a3', 'a4', 'bbz10', 'bbz9', 'bbz8', 'bbz7', 'bbz6', 'bbz5', 'bbz4', 'bbz3', 'bbz2', 'bbz1', 'bb10', 'bb9', 'bb8', 'bb7', 'bb6', 'bb5', 'bb4', 'bb3', 'bb2', 'bb1', 'ba1', 'ba2', 'ba3', 'ba4', 'ba5', 'ba6', 'ba7', 'ba8', 'ba9', 'ba10', 'baz1', 'baz2', 'baz3', 'baz4', 'baz5', 'baz6', 'baz7', 'baz8', 'baz9', 'baz10', 'utcQuoteTime']]
    data[i].columns = ['utcReceiveTime', 'lastPrice', 'volume', ' volumeAcc', 'openInterest', 'bbz1', 'bb1', 'ba1', 'baz1', 'bbz10', 'bbz9', 'bbz8', 'bbz7', 'bbz6', 'bbz5', 'bbz4', 'bbz3', 'bbz2', 'bbz1', 'bb10', 'bb9', 'bb8', 'bb7', 'bb6', 'bb5', 'bb4', 'bb3', 'bb2', 'bb1', 'ba1', 'ba2', 'ba3', 'ba4', 'ba5', 'ba6', 'ba7', 'ba8', 'ba9', 'ba10', 'baz1', 'baz2', 'baz3', 'baz4', 'baz5', 'baz6', 'baz7', 'baz8', 'baz9', 'baz10', 'utcQuoteTime']
for i in range(len(l)):
	dirname = '\\\\172.30.50.120\\temp\\CME_COMEX\\' + l[i]
	if not os.path.isdir(dirname):
		os.mkdir(dirname)
	filename = dirname + "\\" + l[i] + '-' + date +'-N.tick'
	data[i].to_csv(filename, index=False)