import numpy as np
from pymongo import MongoClient
from view.chart import get_chart
import matplotlib.pyplot as plt

client_mongo = MongoClient('localhost', 27017)
db = client_mongo['History']
close_list = db['BTCUSDT'].find({"timeframe":'5m'}, {'candles'})
x = list(close_list)[0]['candles']
for i in range(len(x)):
    range_ts = x[i+1]['time'] - x[i]['time']
    if range_ts > 300000:
        print(x[i-5:i+5])
        print(range_ts, x[i]['time'])