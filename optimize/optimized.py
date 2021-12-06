import math
import multiprocessing

from numpy import arange
import json
from data.get_data import get_data_opt, func_chunks_generators
from multiprocessing import Pool
import time
from optimize.get_optimize import get_moving, trade_spread
import os.path
from pymongo import MongoClient
from config import config
import numpy as np

from utils.utils import get_today_date


ma_num = "0"

start_date = "01.02.2021"

end_date = "23.09.2021"

ma_period_opt = 'all'
deviation_level = 'all'


# Задаем параметры систем


def optimize(data_name_pair: list):
    with open(f'../market_data/data_opt_{start_date}_{end_date}.txt') as json_file:
        data = json.load(json_file)
    levels_param = np.around(arange(0.01, 0.082, 0.002), 3)
    ma_param = range(10, 420, 20)
    for namepair in data_name_pair:
        client_mongo = MongoClient('localhost', 27017)
        db = client_mongo['OptimizedData']
        collection = 'optimized_' + config.ma_type[ma_num]
        name_pair1 = db[collection].find({'NamePair': namepair})
        # Проверка наличия существующий оптимизированных пар not list(name_pair1)
        if not list(name_pair1):
            source1 = np.array(data[namepair[0]])
            source2 = np.array(data[namepair[1]])
            spread = np.around((source1 / source2), 5)
            source2 = source2.tolist()
            source1 = source1.tolist()
            levels_dict = {}
            if deviation_level == 'all':
                for deviation in levels_param:
                    levels = spread * deviation
                    levels_dict[deviation] = levels
            elif deviation_level != 'all':
                levels = spread * float(deviation_level)
                levels_dict[deviation_level] = levels
            ma_dict = get_moving(ma_param, spread, ma_num, ma_period_opt)
            levels_ma = [levels_dict, ma_dict]
            start_time = time.time()
            eq = []
            buy1 = trade_spread(source2, source1, levels_ma, 1, 100, eq, 1)
            if not math.isnan(buy1[0][0]['Profit']):
                sell1 = trade_spread(source1, source2, levels_ma, -1, 100, buy1[1], 1)
                if not math.isnan(sell1[0][0]['Profit']):
                    buy2 = trade_spread(source2, source1, levels_ma, 1, 100, sell1[1], 2)
                    sell2 = trade_spread(source1, source2, levels_ma, -1, 100, buy2[1], 2)
                    print(buy1[0])
                    print(buy2[0])
                    print(sell1[0])
                    print(sell2[0])
                    print(namepair)
                    level_opt_param = {
                        'NamePair': namepair,
                        'TypeMA': config.ma_type[ma_num],
                        'Levelbuy1': buy1[0][0],
                        'Levelbuy2': buy2[0][0],
                        'Levelsell1': sell1[0][0],
                        'Levelsell2': sell2[0][0],
                        'equty': str(sell2[1])
                    }
                    client_mongo = MongoClient('localhost', 27017)
                    db = client_mongo['OptimizedData']
                    collection = 'optimized_' + config.ma_type[ma_num] + "_" + start_date + "_" + end_date
                    db[collection].update_one({'NamePair': namepair}, {"$set": level_opt_param}, True)
            print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    if not os.path.isfile(f'../market_data/data_opt_{start_date}_{end_date}.txt'):
        data = get_data_opt(start_date, end_date, '5m')
        with open(f'../market_data/data_opt_{start_date}_{end_date}.txt', 'w') as outfile:
            json.dump(data, outfile)
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['OptimizedData']
    collection = 'rough_opt_' + config.ma_type[ma_num]
    name_pair_rough = db[collection].find({'TypeMA': config.ma_type[ma_num]}, {'Source1', 'Source2'})
    data_name = list(name_pair_rough)
    source1 = data_name[0]['Source1']
    source2 = data_name[0]['Source2']
    name_pair = []
    for i, j in zip(source1, source2):
        name_pair.append([i, j])
    pair_list_tuple = list(func_chunks_generators(name_pair, 20))
    with Pool(multiprocessing.cpu_count()-2) as p:
        answer = p.map(optimize, pair_list_tuple)
