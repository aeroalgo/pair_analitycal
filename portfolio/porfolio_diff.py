import json

from pymongo import MongoClient
from config import config
import numpy as np
from view.chart import get_chart
from metrics.get_metrics import profit_per_day, dd_abs,dd_percent

ma_num = '0'
size = 200
q_algo = 140
p_sorted = 30
leverage = 10
start_date = "01.02.2021"
end_date = '07.09.2021'

client_mongo = MongoClient('localhost', 27017)
db = client_mongo['OptimizedData']
collection = 'diff_optimized_' + config.ma_type[ma_num] + "_" + start_date + "_" + end_date
sort_colletion = db[collection].find({'Levelsell2.RF': {'$gte': 3}}, {'NamePair', 'Levelbuy2', 'Levelsell2'}).sort(
    'Levelsell2.RF', -1)
sort_colletion = list(sort_colletion)
sort_colletion_pair = []
for i in sort_colletion:
    bad_result = (i['Levelbuy2']['% Вad result'] + i['Levelsell2']['% Вad result']) / 2
    r2 = i['Levelsell2']['R2']
    profit = i['Levelsell2']['Profit']
    if bad_result < p_sorted:
        sort_colletion_pair.append(i['NamePair'])

ticker_portfolio = []
ticker_portfolio2 = []
name_pair_portfolio = []
count = 0
while count < q_algo:
    ticker = []
    name_pair = []
    for i in sort_colletion_pair:
        if i[0] not in ticker and i[1] not in ticker and count < q_algo:
            ticker.append(i[0])
            ticker.append(i[1])
            ticker_portfolio2.append(i[0])
            ticker_portfolio2.append(i[1])
            name_pair.append(i)
            sort_colletion_pair.remove(i)
            count += 1
    ticker_portfolio.append(ticker)
    name_pair_portfolio.append(name_pair)
eq = db[collection].find({'NamePair': name_pair_portfolio[0][0]}, {'equty'})
eq = list(eq)[0]['equty']
eq = json.loads(eq)
# len(np.array(list(eq)[0]['equty']))
cm_eq = np.zeros(len(eq))
name_pair = []
for i in name_pair_portfolio:
    for j in i:
        name_pair.append(j)
        eq = db[collection].find({'NamePair': j}, {'equty'})
        eq = list(eq)[0]['equty']
        eq = json.loads(eq)
        equty = np.array(eq)

        cm_eq = cm_eq + equty

dd_abs = dd_abs(cm_eq)
dd_pct = dd_percent(cm_eq,q_algo,size,leverage)
p_day = profit_per_day(cm_eq, q_algo, size, leverage)

portfolio_name = {
    'MA': config.ma_type[ma_num],
    'PortfolioNamePair': name_pair
}
print('DD =', min(dd_abs))
print('RF =', abs(cm_eq[- 1] / min(dd_abs)))
db['diff_Portfolios'].update_one({'MA': config.ma_type[ma_num]}, {"$set": portfolio_name}, True)
get_chart([cm_eq, dd_abs, dd_pct, p_day])
