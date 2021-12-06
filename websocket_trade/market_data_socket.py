import asyncio
import multiprocessing
import time
import datetime
import requests

from config import config
from db_insert.insert_mongodb import update_mongo_id
from websocket_trade.service_download_history import load_history
from binance import AsyncClient, BinanceSocketManager, Client
import redis
from pymongo import MongoClient


def main_bid_ask(ticker):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(bid_ask(ticker))


def main_candle(ticker, socket_send):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(candle(ticker, socket_send))


async def candle(ticker, socket_send):
    global client
    tiker_cline = []
    for i in ticker:
        tiker_cline.append(i.lower() + '@kline_5m')
    try:
        client_mongo = MongoClient('localhost', 27017)
        db = client_mongo['MarketData']
        collection = 'MarketData'
        client = await AsyncClient.create()
        bm = BinanceSocketManager(client)
        ts = bm.futures_multiplex_socket(tiker_cline)
        r1 = redis.Redis(host='127.0.0.1', port=6379, db=1)
        time_start = datetime.datetime.now()
        time_start = int(time.mktime(time_start.timetuple()))
        count = 0
        try:
            async with ts as tscm:
                while True:
                    res = await asyncio.wait_for(tscm.recv(), timeout=20)
                    res = res['data']
                    if not res['k']['x']:
                        data_candle_dict = {
                            'o': res['k']['o'],
                            'h': res['k']['h'],
                            'l': res['k']['l'],
                            'c': res['k']['c'],
                            'i': res['k']['i'],
                            't': res['k']['t'],

                        }
                        r1.hmset(res['s'], data_candle_dict)
                    if res['k']['x']:
                        data = {
                            't': [res['k']['t']],
                            'open': [float(res['k']['o'])],
                            'high': [float(res['k']['h'])],
                            'low': [float(res['k']['l'])],
                            'close': [float(res['k']['c'])],
                        }
                        timestamp = list(db[collection].find({'_id': res['s']}, {'t'}))
                        try:
                            timestamp = timestamp[0]['t'][-1]
                        except:
                            timestamp = 0
                        if res['k']['t'] != timestamp:
                            update_mongo_id(res['s'], db, collection, data, None, None)
                    time_now = datetime.datetime.now()
                    time_now = int(time.mktime(time_now.timetuple()))
                    if time_now - time_start == 10 and count == 0:
                        count += 1
                        socket_send.append('SocketConnection')
                        print('Socket Connection')
                        print('Download history...')
        except:
            await client.close_connection()

    except:
        await client.close_connection()


def history(ticker, socket_send):
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['TradeAnalyticalData']
    collection = 'system_message'
    time.sleep(5)
    while True:
        if socket_send[-1] == 'SocketConnection':
            load_history(ticker)
            break
        time.sleep(1)
    db[collection].update_one({'_id': 'socket_message'}, {"$set": {'message': 'Connection opened'}}, True)
    print('Connection opened')


async def bid_ask(ticker):
    global client
    tiker_bid_ask = []
    for i in ticker:
        tiker_bid_ask.append(i.lower() + '@bookTicker')
    try:
        client = await AsyncClient.create()
        bm = BinanceSocketManager(client)
        ts = bm.futures_multiplex_socket(tiker_bid_ask)
        r = redis.Redis(host='127.0.0.1', port=6379, db=0)
        try:
            async with ts as tscm:
                while True:
                    res = await asyncio.wait_for(tscm.recv(), timeout=20)
                    res = res['data']
                    bid_ask_dict = {
                        'bid': res['b'],
                        'ask': res['a']
                    }
                    r.hmset(res['s'], bid_ask_dict)
        except:
            await client.close_connection()
    except:
        await client.close_connection()


def main_websocket():
    client = Client(config.API_KEY, config.API_SECRET)
    prices_futures = client.futures_exchange_info()
    ticker = []
    stoplist = ['BTCSTUSDT']
    for price in prices_futures['symbols']:
        if price['symbol'] not in stoplist:
            ticker.append(price['symbol'])
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['system_message']
    collection = 'system_message'
    db[collection].update_one({'_id': 'socket_message'}, {"$set": {'message': 'Connection closed'}}, True)
    while True:
        message = db[collection].find({'_id': 'socket_message'}, {'message'})
        with multiprocessing.Manager() as manager:
            socket_send = manager.list([0])
            p1 = multiprocessing.Process(name='bid_ask_socket', target=main_bid_ask, args=(ticker,))
            p2 = multiprocessing.Process(name='candle_socket', target=main_candle, args=(ticker, socket_send,))
            p3 = multiprocessing.Process(name='dw_history', target=history, args=(ticker, socket_send,))
            try:
                status = requests.get('https://www.google.com/').status_code
                if list(message)[0]['message'] == 'Connection closed':
                    p1.start()
                    p2.start()
                    p3.start()
                    if p1.join() is None or p2.join() is None:
                        db[collection].update_one({'_id': 'socket_message'}, {"$set": {'message': 'Connection closed'}},
                                                  True)
                        print('Connection Error')
                        p1.terminate()
                        p2.terminate()
                        p3.terminate()
                        time.sleep(5)
            except:
                time.sleep(2)
                print('Internet connection error')


if __name__ == "__main__":
    main_websocket()
