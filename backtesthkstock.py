df = arm.sort(['Date','Rank'], ascending=[1,0])
df['Ticker'] = df.Ticker.apply(lambda x: str(x).rjust(4,'0')+'.HK')

for i in dates:
    long_stocks.append(list(df[df['Date'] == i].iloc[:10].Ticker))
for i in dates:
    short_stocks.append(list(df[df['Date'] == i].iloc[-10:].Ticker))

money = list()

profit_long = list()

profit_short = list()

date = list()

for i in range(len(dates)-1):
    start = dates[i]
    end = dates[i+1]
    try:
        print dates[i]
        m = -1000000
        for j in long_stocks[i]:
            a = data.DataReader(j, 'yahoo', start, end)
            m = m + 100000/a['Adj Close'][0]*a['Adj Close'][-1]
        print m
        n = 1000000
        for j in short_stocks[i]:
            a = data.DataReader(j, 'yahoo', start, end)
            n = n - 100000/a['Adj Close'][0]*a['Adj Close'][-1]
        print n
    except:
        continue
    money.append(m+n)
    profit_long.append(m)
    profit_short.append(n)
    date.append(dates[i])
    