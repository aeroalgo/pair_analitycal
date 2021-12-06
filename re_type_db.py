from pymongo import MongoClient
from config import config

client_mongo = MongoClient('localhost', 27017)
db = client_mongo['OptimizedData']
for i in config.ma_type:
    collection = 'optimized_' + config.ma_type[i]
    name_doc = db[collection].find({'TypeMA': config.ma_type[i]})
    for j in list(name_doc):
        level_opt_param = {
            'NamePair': j['NamePair'],
            'TypeMA': j['TypeMA'],
            'Levelbuy1': j['Levelbuy1'],
            'Levelbuy2': j['Levelbuy2'],
            'Levelsell1': j['Levelsell1'],
            'Levelsell2': j['Levelsell2'],
            'equty': str(j['equty'])
        }
        db[collection].update_one({'NamePair': j['NamePair']}, {"$set": level_opt_param}, True)
