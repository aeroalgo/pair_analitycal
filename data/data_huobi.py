import requests
import codecs
import json
import re
from binance import Client
from pymongo import MongoClient
from datetime import datetime
from config import config
from datetime import timezone
from utils.utils import get_today_date
from tqdm import tqdm

# client_mongo = MongoClient('localhost', 27017)
# db = client_mongo['History']
# dt_obj_st = datetime.strptime(start_date + ' 00:00:00,00',
#                               '%d.%m.%Y %H:%M:%S,%f')
# dt_obj_end = datetime.strptime(end_date + ' 00:00:00,00',
#                                '%d.%m.%Y %H:%M:%S,%f')
# start_date_ts = int(dt_obj_st.replace(tzinfo=timezone.utc).timestamp()) * 1000
# end_date_ts = int(dt_obj_end.replace(tzinfo=timezone.utc).timestamp()) * 1000
response = requests.get('https://api.hbdm.com/linear-swap-api/v1/swap_contract_info')
response = response.content
client = Client(config.API_KEY, config.API_SECRET)
prices_spot = client.get_all_tickers()

get_market_data = codecs.decode(response, 'UTF-8')
get_market_data = json.loads(get_market_data)
#     timeframe_dict = {
#         '1m': Client.KLINE_INTERVAL_1MINUTE,
#         '5m': Client.KLINE_INTERVAL_5MINUTE,
#         '15m': Client.KLINE_INTERVAL_15MINUTE,
#         '4H': Client.KLINE_INTERVAL_4HOUR,
#         '1D': Client.KLINE_INTERVAL_1DAY
#     }
#     stamp_interval = {
#         '1m': 1 * 60 * 1000,
#         '5m': 5 * 60 * 1000,
#         '15m': 15 * 60 * 1000,
#         '4H': 240 * 60 * 1000,
#         '1D': 24 * 60 * 60 * 1000
#     }
symbol_spot_binance = []
symbol_futures_okex = []
for price in prices_spot:
    symbol = price['symbol']
    if symbol[-4:] == 'USDT':
        symbol_spot_binance.append(symbol)
count = 0
for val, data in enumerate(get_market_data['data'], 0):
    symbol_huobi = re.sub('[^0-9a-zA-Z]+', '', data["contract_code"])
    if symbol_huobi in symbol_spot_binance:
        count += 1
        print(count)
        print(symbol_huobi)
#                 symbol_futures_okex.append(symbol_okex[:-4])
#     db = client_mongo['History_okex']
#     for symbol in tqdm(symbol_futures_okex):
#         data_db = db[symbol].find({'timeframe': timeframe})
#         if not list(data_db):
#             klines = client.get_historical_klines(symbol, timeframe_dict[timeframe], start_date_ts, end_date_ts)
#             data_klines = {
#                 '_id': symbol + '_' + timeframe,
#                 'timeframe': timeframe,
#                 'candles': []
#             }
#             for kline in klines:
#                 candle = {
#                     'time': kline[0],
#                     'open': float(kline[1]),
#                     'high': float(kline[2]),
#                     'low': float(kline[3]),
#                     'close': float(kline[4]),
#                 }
#                 data_klines['candles'].append(candle)
#             db[symbol].insert_one(data_klines)
#
#         data_db = list(db[symbol].find({'timeframe': timeframe}))[0]
#         start_date_ts_dict = {
#             'time': start_date_ts
#         }
#         end_date_ts_dict = {
#             'time': end_date_ts
#         }
#         data_db['candles'].insert(0, start_date_ts_dict)
#         data_db['candles'].append(end_date_ts_dict)
#         index_count = -1
#         for i in data_db['candles']:
#             if index_count != len(data_db['candles']) * -1:
#                 if data_db['candles'][index_count]['time'] - data_db['candles'][index_count - 1]['time'] > \
#                         stamp_interval[timeframe]:
#                     if index_count == -1:
#                         klines = client.get_historical_klines(symbol, timeframe_dict[timeframe],
#                                                               data_db['candles'][index_count - 1]['time'] +
#                                                               stamp_interval[
#                                                                   timeframe],
#                                                               data_db['candles'][index_count]['time'])
#                         for kline in klines:
#                             candle = {
#                                 'time': kline[0],
#                                 'open': float(kline[1]),
#                                 'high': float(kline[2]),
#                                 'low': float(kline[3]),
#                                 'close': float(kline[4]),
#                             }
#                             data_db['candles'].insert(index_count, candle)
#
#                     if index_count != -1:
#                         klines = client.get_historical_klines(symbol, timeframe_dict[timeframe],
#                                                               data_db['candles'][index_count - 1]['time'] +
#                                                               stamp_interval[timeframe],
#                                                               data_db['candles'][index_count]['time'])
#                         for i in range(len(klines) - 1):
#                             candle = {
#                                 'time': klines[i][0],
#                                 'open': float(klines[i][1]),
#                                 'high': float(klines[i][2]),
#                                 'low': float(klines[i][3]),
#                                 'close': float(klines[i][4]),
#                             }
#                             data_db['candles'].insert(index_count, candle)
#             index_count += -1
#         data_db['candles'].pop(0)
#         data_db['candles'].pop(-1)
#         db[symbol].update_one({'_id': symbol + '_' + timeframe}, {"$set": data_db}, True)
#     return 'Download ОК'
#
#
# if __name__ == '__main__':
#     start_date = str(input("Введите дату начала загружаемого периода в формате ДД.ММ.ГГГГ(по умолчанию установлено "
#                            "01.01.2021)") or '01.01.2021')
#
#     end_date = str(
#         input("Введите дату окончания загружаемого периода в формате ДД.ММ.ГГГГ(по умолчанию текущая дата)")
#         or get_today_date())
#
#     timeFrame = str(input('Введите таймфрейм(по умолчанию 5 минут)') or '5m')
#     x = get_history(start_date, end_date, timeFrame)
