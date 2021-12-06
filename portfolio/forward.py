from portfolio.get_forward import trade_spread
from metrics.get_metrics import dd_abs, profit_per_day, dd_percent, profit_pct
import numpy as np
import json
from data.get_data import get_data_opt, get_name_pair
from optimize.get_optimize import get_moving
import os.path
from pymongo import MongoClient
from config import config
from utils.utils import get_today_date
from view.chart import get_chart
import matplotlib.pyplot as plt
from tqdm import tqdm

ma_num = str(input("Введите номер скользящей стредней"))

start_date = '01.08.2021'
end_date = str(get_today_date())


start_date_f = "01.02.2021"
end_date_f = '07.09.2021'
ma_param = range(10, 400, 20)

levelsMap = [
    {
        "param1": "Levelbuy1",
        "action": 1
    }, {
        "param1": "Levelsell1",
        "action": -1
    }, {
        "param1": "Levelbuy2",
        "action": 1
    }, {
        "param1": "Levelsell2",
        "action": -1
    }
]


def getLevelData(spread, deviation_level, ma_param, ma_period_opt):
    levels_dict = {}
    levels = spread * float(deviation_level)
    levels_dict[deviation_level] = levels
    ma_dict = get_moving(ma_param, spread, ma_num, ma_period_opt)
    return [levels_dict, ma_dict]


def optimize(data_name_pair: list):
    with open(f'../market_data/data_opt_{start_date}_{end_date}.txt') as json_file:
        data = json.load(json_file)
    eqi = np.zeros(len(data[data_name_pair[0][0]]) + 1)
    pair = get_name_pair(data)
    for namepair in tqdm(data_name_pair):
        source1 = np.array(data[namepair[0]])
        source2 = np.array(data[namepair[1]])
        spread = np.around((source1 / source2), 5)
        source2 = source2.tolist()
        source1 = source1.tolist()
        client_mongo = MongoClient('localhost', 27017)
        db = client_mongo['OptimizedData']
        collection = 'optimized_' + config.ma_type[ma_num] + "_" + start_date_f + "_" + end_date_f
        param = db[collection].find({'NamePair': namepair},
                                    {'Levelbuy1.MA Period', 'Levelbuy1.MA Type', 'Levelbuy1.Dev',
                                     'Levelbuy2.MA Period', 'Levelbuy2.MA Type', 'Levelbuy2.Dev',
                                     'Levelsell1.MA Period', 'Levelsell1.MA Type', 'Levelsell1.Dev',
                                     'Levelsell2.MA Period', 'Levelsell2.MA Type', 'Levelsell2.Dev'})
        param = list(param)[0]
        resultEquity = []

        for item in levelsMap:
            ma_period_opt = param[item["param1"]]['MA Period']
            deviation_level = param[item["param1"]]["Dev"]
            levels_ma = getLevelData(spread, deviation_level, ma_param, ma_period_opt)
            src1 = source2 if item["action"] == 1 else source1
            src2 = source1 if item["action"] == 1 else source2
            resultEquity = trade_spread(src1, src2, levels_ma, item['action'], 100, resultEquity)

        eqi = eqi + np.array(resultEquity)
        plt.plot(resultEquity)
    return eqi


if __name__ == '__main__':
    if not os.path.isfile(f'../market_data/data_opt_{start_date}_{end_date}.txt'):
        data = get_data_opt(start_date, end_date, '5m')
        with open(f'../market_data/data_opt_{start_date}_{end_date}.txt', 'w') as outfile:
            json.dump(data, outfile)
    client_mongo = MongoClient('localhost', 27017)
    db = client_mongo['OptimizedData']
    collection = 'Portfolios'
    data_pair = db[collection].find({'MA': config.ma_type[ma_num]}, {'PortfolioNamePair'})
    data_pair = list(data_pair)[0]['PortfolioNamePair']
    answer = optimize(data_pair)
    dd = dd_percent(answer, len(data_pair), 200, 10)
    pd = profit_per_day(answer, len(data_pair), 200, 10)
    ppct = profit_pct(answer, len(data_pair), 200, 10)
    get_chart([answer, dd, pd])
