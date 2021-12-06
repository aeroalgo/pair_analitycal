import json

from pymongo import MongoClient

# start_date = '01.02.2021'
# end_date = '20.07.2021'
# with open(f'../market_data/data_opt_{start_date}_{end_date}.txt') as json_file:
#     data = json.load(json_file)
# for i in range(len(data['BTCUSDT']) - 1):
#     print(data['BTCUSDT'][i + 1] - data['BTCUSDT'][i])
client_mongo = MongoClient('localhost', 27017)
db = client_mongo['History']
list_collection = db.list_collection_names()
for i in list_collection:
    if i == 'BTCUSDT':
        x = list(db[i].find({}, {'t'}))
        for j in range(len(x[0]['t']) - 1):
            y = x[0]['t'][j + 1] - x[0]['t'][j]
            if y != 300000:
                print(x[0]['t'][j], y)
