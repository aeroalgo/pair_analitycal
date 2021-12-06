from pymongo import MongoClient
from datetime import datetime
from config import config
from binance.client import Client
from utils.utils import get_today_date
from tqdm import tqdm
from db_insert.insert_mongodb import update_mongo_id
from datetime import timezone

stop_list = ['BTCSTUSDT']


def get_history(start_date: str, end_date: str, timeframe: str):
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['History']
    list_collection = db.list_collection_names()
    dt_obj_st = datetime.strptime(start_date + ' 00:00:00,00',
                                  '%d.%m.%Y %H:%M:%S,%f')
    dt_obj_end = datetime.strptime(end_date + ' 00:00:00,00',
                                   '%d.%m.%Y %H:%M:%S,%f')
    start_date_ts = int(dt_obj_st.replace(tzinfo=timezone.utc).timestamp()) * 1000
    end_date_ts = int(dt_obj_end.replace(tzinfo=timezone.utc).timestamp()) * 1000
    timeframe_dict = {
        '1m': Client.KLINE_INTERVAL_1MINUTE,
        '5m': Client.KLINE_INTERVAL_5MINUTE,
        '15m': Client.KLINE_INTERVAL_15MINUTE,
        '4H': Client.KLINE_INTERVAL_4HOUR,
        '1D': Client.KLINE_INTERVAL_1DAY
    }
    stamp_interval = {
        '1m': 1 * 60 * 1000,
        '5m': 5 * 60 * 1000,
        '15m': 15 * 60 * 1000,
        '4H': 240 * 60 * 1000,
        '1D': 24 * 60 * 60 * 1000
    }
    symbol_futures = []
    symbol_spot = []
    symbol_futures_data = []
    client = Client(config.API_KEY, config.API_SECRET)
    prices_futures = client.futures_exchange_info()
    prices_spot = client.get_all_tickers()
    for price in prices_futures['symbols']:
        symbol_futures.append(price['symbol'])
    for price in prices_spot:
        symbol = price['symbol']
        if symbol[-4:] == 'USDT':
            symbol_spot.append(symbol)
    for i in symbol_futures:
        for j in symbol_spot:
            if i == j:
                symbol_futures_data.append(j)
                break
    for i in symbol_futures_data:
        if i not in list_collection and i not in stop_list:
            db.create_collection(i)
    for symbol in tqdm(symbol_futures_data):
        if symbol not in stop_list:
            data_db = db[symbol].find({'timeframe': timeframe})
            if not list(data_db):
                klines = client.get_historical_klines(symbol, timeframe_dict[timeframe], start_date_ts, end_date_ts)
                data_klines = {
                    '_id': symbol + '_' + timeframe,
                    'timeframe': timeframe,
                    'candles': []
                }
                for kline in klines:
                    candle = {
                        'time': kline[0],
                        'open': float(kline[1]),
                        'high': float(kline[2]),
                        'low': float(kline[3]),
                        'close': float(kline[4]),
                    }
                    data_klines['candles'].append(candle)
                db[symbol].insert_one(data_klines)

            data_db = list(db[symbol].find({'timeframe': timeframe}))[0]
            start_date_ts_dict = {
                'time': start_date_ts
            }
            end_date_ts_dict = {
                'time': end_date_ts
            }
            data_db['candles'].insert(0, start_date_ts_dict)
            data_db['candles'].append(end_date_ts_dict)
            index_count = -1
            for i in data_db['candles']:
                if index_count != len(data_db['candles']) * -1:
                    if data_db['candles'][index_count]['time'] - data_db['candles'][index_count - 1]['time'] > \
                            stamp_interval[timeframe]:
                        if index_count == -1:
                            klines = client.get_historical_klines(symbol, timeframe_dict[timeframe],
                                                                  data_db['candles'][index_count - 1]['time'] +
                                                                  stamp_interval[
                                                                      timeframe],
                                                                  data_db['candles'][index_count]['time'])
                            for kline in klines:
                                candle = {
                                    'time': kline[0],
                                    'open': float(kline[1]),
                                    'high': float(kline[2]),
                                    'low': float(kline[3]),
                                    'close': float(kline[4]),
                                }
                                data_db['candles'].insert(index_count, candle)

                        if index_count != -1:
                            klines = client.get_historical_klines(symbol, timeframe_dict[timeframe],
                                                                  data_db['candles'][index_count - 1]['time'] +
                                                                  stamp_interval[timeframe],
                                                                  data_db['candles'][index_count]['time'])
                            for i in range(len(klines) - 1):
                                candle = {
                                    'time': klines[i][0],
                                    'open': float(klines[i][1]),
                                    'high': float(klines[i][2]),
                                    'low': float(klines[i][3]),
                                    'close': float(klines[i][4]),
                                }
                                data_db['candles'].insert(index_count, candle)
                index_count += -1
            data_db['candles'].pop(0)
            data_db['candles'].pop(-1)
            db[symbol].update_one({'_id': symbol + '_' + timeframe}, {"$set": data_db}, True)
    return 'Download ОК'


def get_data_opt(start_date: str, end_date: str, timeframe: str):
    # Date format 01.01.2021
    dt_obj_st = datetime.strptime(start_date + ' 00:00:00,00',
                                  '%d.%m.%Y %H:%M:%S,%f')
    dt_obj_end = datetime.strptime(end_date + ' 00:00:00,00',
                                   '%d.%m.%Y %H:%M:%S,%f')
    start_date_tp = int(dt_obj_st.replace(tzinfo=timezone.utc).timestamp()) * 1000
    end_date_tp = int(dt_obj_end.replace(tzinfo=timezone.utc).timestamp()) * 1000
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['History']
    collection_name = db.list_collection_names()
    history = {}
    for symbol in tqdm(collection_name):
        timestamp_db = db[symbol].find({'timeframe': timeframe}, {'candles'})
        data = {
            'time': [],
            'close': []
        }
        try:
            for obj in list(timestamp_db)[0]['candles']:
                data['time'].append(obj['time'])
                data['close'].append(obj['close'])
            index_start_date = data['time'].index(start_date_tp)
            index_end_date = data['time'].index(end_date_tp)                                                                                                                                
            close = data['close'][index_start_date:index_end_date]
            history[symbol] = close
        except (ValueError, IndexError):
            print(symbol, ' no history from this date')
    data_json = {}
    for i in history:
        x = list(map(float, history[i]))
        data_json[i] = x
    return data_json


def get_name_pair(data):
    name_ticker = []
    for name in data:
        name_ticker.append(name)
    name_pair = []
    for i in range(len(name_ticker)):
        for j in range(i + 1, len(name_ticker) - 1):
            name_pair.append([name_ticker[i], name_ticker[j]])
    return name_pair


def func_chunks_generators(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i: i + n]


if __name__ == '__main__':
    start_date = str(input("Введите дату начала загружаемого периода в формате ДД.ММ.ГГГГ(по умолчанию установлено "
                           "01.01.2021)") or '01.01.2021')

    end_date = str(input("Введите дату окончания загружаемого периода в формате ДД.ММ.ГГГГ(по умолчанию текущая дата)")
                   or get_today_date())

    timeFrame = str(input('Введите таймфрейм(по умолчанию 5 минут)') or '5m')
    x = get_history(start_date, end_date, timeFrame)
