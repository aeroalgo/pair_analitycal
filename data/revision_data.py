from utils.utils import get_today_date
import json

start_date = '01.02.2021'

end_date = str(get_today_date())

with open(f'../market_data/data_opt_{start_date}_{end_date}.txt') as json_file:
    data = json.load(json_file)
for i in data:
    print(i, len(data[i]))
