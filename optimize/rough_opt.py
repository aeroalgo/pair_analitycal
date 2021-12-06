import multiprocessing
import json
import os.path
from optimize.get_optimize import trade_spread_rough
import pandas as pd
import time
import numpy as np
from data.get_data import get_name_pair
from config import config
from multiprocessing import Pool
import talib
from pymongo import MongoClient
from data.get_data import get_data_opt, func_chunks_generators
from utils.utils import get_today_date

ma_num = '0'

start_date = '01.02.2021'

end_date = str(get_today_date())


def opt(source: list):
    with open(f'../market_data/data_opt_{start_date}_{end_date}.txt') as json_file:
        data = json.load(json_file)
    opt_list = {}
    s1 = []
    s2 = []
    p = []
    ma_period = 100
    for name in source:
        source1 = np.array(data[name[0]])
        source2 = np.array(data[name[1]])
        spread = np.around((source1 / source2), 5)
        ma_type = {
            '6': talib.DEMA(spread, ma_period),
            '1': talib.EMA(spread, ma_period),
            '5': (3 * talib.WMA(spread, ma_period) - 2 * talib.SMA(spread, ma_period)),
            '4': talib.KAMA(spread, ma_period),
            '0': talib.SMA(spread, ma_period),
            '8': talib.T3(spread, ma_period),
            '7': talib.TEMA(spread, ma_period),
            '2': talib.WMA(spread, ma_period)
        }
        sma_spread = ma_type[ma_num]
        kat = spread * 0.015
        indicator_spread = spread - sma_spread
        source1 = source1.tolist()
        source2 = source2.tolist()
        ind = indicator_spread.tolist()
        kat = kat.tolist()
        buy1 = trade_spread_rough(source2, source1, ind, kat, 1, 1, 100)
        sell1 = trade_spread_rough(source1, source2, ind, kat, 1, -1, 100)
        s1.append(name[0])
        s2.append(name[1])
        p.append(buy1 + sell1)
        opt_list['Source1'] = s1
        opt_list['Source2'] = s2
        opt_list['Profit'] = p
    return opt_list


def main():
    if not os.path.isfile(f'../market_data/data_opt_{start_date}_{end_date}.txt'):
        data = get_data_opt(start_date, end_date, '5m')
        with open(f'../market_data/data_opt_{start_date}_{end_date}.txt', 'w') as outfile:
            json.dump(data, outfile)
    with open(f'../market_data/data_opt_{start_date}_{end_date}.txt') as json_file:
        data = json.load(json_file)
    start_time = time.time()
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['OptimizedData']
    list_collection = db.list_collection_names()
    name_collection = 'rough_opt_' + config.ma_type[ma_num]
    if name_collection not in list_collection:
        db.create_collection(name_collection)
    pair_list_tuple = get_name_pair(data)
    pair_list_tuple = list(func_chunks_generators(pair_list_tuple, 30))
    with Pool(multiprocessing.cpu_count()-3) as p:
        answer = p.map(opt, pair_list_tuple)
    source1 = []
    source2 = []
    profit = []
    for i in answer:
        source1 += i['Source1']
        source2 += i['Source2']
        profit += i['Profit']
    data = {
        'TypeMA': config.ma_type[ma_num],
        'Source1': source1,
        'Source2': source2,
        'Profit': profit
    }
    data_sort = pd.DataFrame(data).sort_values('Profit', ascending=False)
    data_sort = data_sort[data_sort['Profit'] > 0]
    data_sort_dict = data_sort.to_dict(orient='list')
    db[name_collection].update_one({'TypeMA': config.ma_type[ma_num]}, {"$set": data_sort_dict}, True)
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()
