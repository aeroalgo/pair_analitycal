from pymongo import MongoClient

client_mongo = MongoClient('localhost', 27017)
db = client_mongo['History']
candles = db['BTCUSDT'].find({"timeframe": '4H'}, {'candles'})
candles = list(candles)[0]['candles']
tr1 = 0
tr2 = 0
tr3 = 0
true_range = []
per = 155
atr = []
for i in range(len(candles)):
    if i == 0:
        tr1 = candles[i]['high'] - candles[i]['low']
        true_range.append(max(tr1, tr2, tr3))

    else:
        tr1 = candles[i]['high'] - candles[i]['low']
        tr2 = abs(candles[i]['high'] - candles[i-1]['close'])
        tr2 = abs(candles[i]['low'] - candles[i-1]['close'])
        true_range.append(max(tr1, tr2, tr3))

for i in range(len(true_range)):
    if i < per:
        atr.append(None)
    else:
        atr.append(sum(true_range[i-per:i])/per)
    print(i, atr[i], candles[i]['close'])