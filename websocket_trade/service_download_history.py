import time
import redis
from binance.enums import HistoricalKlinesType
from pymongo import MongoClient
from db_insert.insert_mongodb import update_mongo_id
import datetime
from binance.client import Client
from config import config
from tqdm import tqdm


def load_history(ticker):
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['MarketData']
    collection = 'MarketData'
    r1 = redis.Redis(host='127.0.0.1', port=6379, db=1, charset="utf-8", decode_responses=True)
    try:
        client = Client(config.API_KEY, config.API_SECRET)
        q_candle = 600
        stamp_interval = 5 * 60 * 1000
        timeframe_dict = {
            '1m': Client.KLINE_INTERVAL_1MINUTE,
            '5m': Client.KLINE_INTERVAL_5MINUTE,
            '15m': Client.KLINE_INTERVAL_15MINUTE,
            '1D': Client.KLINE_INTERVAL_1DAY
        }

        for name in tqdm(ticker):
            now = datetime.datetime.now()
            now = int(time.mktime(now.timetuple()))
            data_last_kline = r1.hgetall(name)
            timestamp_rdb = int(data_last_kline['t'])
            sec_sleep = timestamp_rdb / 1000 + 300 - now - 20
            if sec_sleep < 0:
                time.sleep(25)
            data_ticker = {
                '_id': name,
                'open': [],
                'high': [],
                'low': [],
                'close': [],
                't': [],
            }
            collection_copy = list(db[collection].find({'_id': name}))
            if not collection_copy:
                db[collection].update_one({'_id': name}, {'$set': data_ticker}, True)
            collection_copy = list(db[collection].find({'_id': name}))
            collection_copy_work = collection_copy[0]
            data_last_kline = r1.hgetall(name)
            t_rdb = int(data_last_kline['t'])
            end_dw_candle = t_rdb - stamp_interval * q_candle
            stamp_end = [i for i in range(end_dw_candle, t_rdb, stamp_interval)]
            try:
                for j in range(-1, -len(stamp_end), -1):
                    if stamp_end[j] != collection_copy_work['t'][j]:

                        klines = client.get_historical_klines(name, timeframe_dict['5m'],
                                                                  start_str=collection_copy_work['t'][j],
                                                                  end_str=stamp_end[j],
                                                                  klines_type=HistoricalKlinesType.FUTURES)
                        if j == -1:
                            for kline in range(1, len(klines)):
                                collection_copy_work['open'].append(float(klines[kline][1]))
                                collection_copy_work['high'].append(float(klines[kline][2]))
                                collection_copy_work['low'].append(float(klines[kline][3]))
                                collection_copy_work['close'].append(float(klines[kline][4]))
                                collection_copy_work['t'].append(klines[kline][0])
                        elif j != -1:
                            for kline in range(1, len(klines)):
                                collection_copy_work['open'].insert(j + 1, float(klines[kline][1]))
                                collection_copy_work['high'].insert(j + 1, float(klines[kline][2]))
                                collection_copy_work['low'].insert(j + 1, float(klines[kline][3]))
                                collection_copy_work['close'].insert(j + 1, float(klines[kline][4]))
                                collection_copy_work['t'].insert(j + 1, klines[kline][0])
                        # except:
                        #     db[collection].update_one({'_id': name}, {'$set': data_ticker})
                        #     load_history(ticker)
                        time.sleep(0.2)
            except IndexError:
                st_time = stamp_end[0]
                try:
                    end_time = collection_copy_work['t'][0]
                except IndexError:
                    end_time = t_rdb
                klines = client.get_historical_klines(name, timeframe_dict['5m'],
                                                      start_str=int(st_time),
                                                      end_str=int(end_time + stamp_interval),
                                                      klines_type=HistoricalKlinesType.FUTURES)
                klines.reverse()
                for i in range(len(klines) - 2):
                    collection_copy_work['open'].insert(0, float(klines[i][1]))
                    collection_copy_work['high'].insert(0, float(klines[i][2]))
                    collection_copy_work['low'].insert(0, float(klines[i][3]))
                    collection_copy_work['close'].insert(0, float(klines[i][4]))
                    collection_copy_work['t'].insert(0, klines[i][0])
            db[collection].update_one({'_id': name}, {'$set': data_ticker})
            del collection_copy_work['_id']
            update_mongo_id(name, db, collection, collection_copy_work, q_candle, 0)
    except:
        print('Download history error')
        load_history(ticker)
