from pymongo import MongoClient

from config import config


def is_collection_exist(client_mongo):
    data_base = client_mongo['OptimizedData']
    list_collection = data_base.list_collection_names()
    name_collection = 'TradePortfolios'
    if name_collection not in list_collection:
        data_base.create_collection(name_collection)


def convert_portfolio():
    """This method convert optimization results into trade server model"""
    ma_num = str(input("Введите номер скользящей стредней\n"))
    ma_type = config.ma_type[ma_num]
    converted_collection = []
    client_mongo = MongoClient('localhost', 27017)
    data_base = client_mongo['OptimizedData']
    is_collection_exist(client_mongo)

    collection = 'optimized_' + ma_type
    collectionPortfolios = 'Portfolios'
    portfolio_name_pair = data_base[collectionPortfolios].find({'MA': ma_type}, {'PortfolioNamePair'})
    portfolio_for_convert = list(portfolio_name_pair)[0]['PortfolioNamePair']
    for pair in portfolio_for_convert:
        result = list(data_base[collection].find({'NamePair': [pair[0], pair[1]]}))[0]

        converted_item1 = {
            'ticker1': result['NamePair'][0],
            'ticker2': result['NamePair'][1],
            'longMAType': result['Levelbuy1']['MA Type'],
            'longMA': result['Levelbuy1']['MA Period'],
            'shortMAType': result['Levelsell1']['MA Type'],
            'shortMA': result['Levelbuy1']['MA Period'],
            'shortLevelStepSize': result['Levelsell1']['Dev'],
            'longLevelStepSize': result['Levelbuy1']['Dev'],
        }

        converted_item2 = {
            'ticker1': result['NamePair'][0],
            'ticker2': result['NamePair'][1],
            'longMAType': result['Levelbuy2']['MA Type'],
            'longMA': result['Levelbuy2']['MA Period'],
            'shortMAType': result['Levelsell2']['MA Type'],
            'shortMA': result['Levelbuy2']['MA Period'],
            'shortLevelStepSize': result['Levelsell2']['Dev'],
            'longLevelStepSize': result['Levelbuy2']['Dev'],
        }
        converted_collection.append(converted_item1)
        converted_collection.append(converted_item2)
    result_data_base = client_mongo['TradeAnalyticalData']
    result_data_base['TradePortfolios'].insert_one({'MA': ma_type, 'portfolio': converted_collection})

    print('------------------------------------------------------------------------')


def main():
    """This is a main function that run portfolio converter"""
    convert_portfolio()


if __name__ == "__main__":
    main()
