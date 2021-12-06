from pymongo import MongoClient
from config import config
import sqlite3
import uuid
from config.script_code import code, setting_script, setting_agent


start_date = "01.02.2021"
end_date = '07.09.2021'
portfolio_id = 2
ma_num = '1'
client_mongo = MongoClient('localhost', 27017)
db = client_mongo['OptimizedData']
collection = 'optimized_' + config.ma_type[ma_num] + "_" + start_date + "_" + end_date
data_pair = db['Portfolios'].find({'MA': config.ma_type[ma_num]}, {'PortfolioNamePair'})
data_pair = list(data_pair)[0]['PortfolioNamePair']

conn = sqlite3.connect('D:\Cache.sqlite')
c = conn.cursor()
id_agent = c.execute('''SELECT * FROM Agent ORDER BY AgentId DESC LIMIT 1''')
try:
    id_agent = int(list(id_agent)[0][0] + 1)
except IndexError:
    id_agent = 0
id_map = c.execute('''SELECT * FROM Mapping ORDER BY MappingId DESC LIMIT 1''')
try:
    id_map = int(list(id_map)[0][0] + 1)
except IndexError:
    id_map = 0
id_ag_ev = c.execute('''SELECT * FROM AgentEvent ORDER BY AgentEventId DESC LIMIT 1''')
try:
    id_ag_ev = int(list(id_ag_ev)[0][0] + 1)
except IndexError:
    id_ag_ev = 0
id_script = c.execute('''SELECT * FROM Script ORDER BY ScriptId DESC LIMIT 1''')
id_script = int(list(id_script)[0][0] + 1)

"""Очищает таблицы !!!Не использовать при добавлении нескольких портфелей!!!
                Использовать только при первом добавлении"""
# sql_update_query = """DELETE from Script where ParentId = ?"""
# c.execute(sql_update_query, (572,))
# conn.commit()
c.execute('''DELETE FROM CachedTransactionInfoes''')
conn.commit()
# c.execute('''DELETE FROM Mapping''')
# conn.commit()
# c.execute('''DELETE FROM AgentEvent''')
# conn.commit()
"""Очищает таблицы !!!Не использовать при добавлении нескольких портфелей!!!
                Использовать только при первом добавлении"""

for i in data_pair:
    name_pair = i[0] + '_' + i[1] + '_' + config.ma_type[ma_num]
    sql_update_query = """DELETE from Script where Name = ?"""
    c.execute(sql_update_query, (name_pair,))
    conn.commit()
    param = db[collection].find({'NamePair': i}, {'Levelbuy1.MA Period', 'Levelbuy1.MA Type', 'Levelbuy1.Dev',
                                                  'Levelbuy2.MA Period', 'Levelbuy2.MA Type', 'Levelbuy2.Dev',
                                                  'Levelsell1.MA Period', 'Levelsell1.MA Type', 'Levelsell1.Dev',
                                                  'Levelsell2.MA Period', 'Levelsell2.MA Type', 'Levelsell2.Dev'})
    param = list(param)[0]
    replacecode = code.replace("""
    <Sources>
      <Source DataSourceName="BinanceFutures" SecurityId="ADAUSDT" Name="13E828E4-4633-455C-B81B-730B003D8002" VisualTypeName="Торгуемый инструмент" IsOption="false">
        <Records />
      </Source>
      <Source DataSourceName="BinanceFutures" SecurityId="AVAXUSDT" Name="dae2c52a-3337-4eea-9caf-f302f70848d5" VisualTypeName="Торгуемый инструмент" IsOption="false">
        <Records />
      </Source>
    </Sources>
    <Parameters>
      <Parameter xsi:type="OptimData" ItemName="4a074d54-81cb-4469-bbd7-698000095100" BlockName="НачальныйBuy1" Name="Значение" InvariantName="Value" CodeName="НачальныйBuy1_Value" UsedInOptimization="false" IsCalculable="false" Value="0.024" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="c149f466-7e54-4b9f-b86a-ca97cdda67be" BlockName="НачальныйSell1" Name="Значение" InvariantName="Value" CodeName="НачальныйSell1_Value" UsedInOptimization="false" IsCalculable="false" Value="0.028" TypeName="Double" MinValue="0" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="3ecf4a44-b37b-4080-9acf-3c19e06d771a" BlockName="НачальныйBuy2" Name="Значение" InvariantName="Value" CodeName="НачальныйBuy2_Value" UsedInOptimization="false" IsCalculable="false" Value="0.02" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="104fa729-feab-466a-baed-7a94e61b1417" BlockName="НачальныйSell2" Name="Значение" InvariantName="Value" CodeName="НачальныйSell2_Value" UsedInOptimization="false" IsCalculable="false" Value="0.014" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="IntOptimData" ItemName="5123f484-6315-489f-8063-59b75593c17f" BlockName="_MA_Sell_1" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Sell_1_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="50" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="5123f484-6315-489f-8063-59b75593c17f" BlockName="_MA_Sell_1" Name="MAType" InvariantName="MAType" CodeName="_MA_Sell_1_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="2f3a13c8-9c42-4cac-90ed-36a8aabe926f" BlockName="_MA_Buy1" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Buy1_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="10" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="2f3a13c8-9c42-4cac-90ed-36a8aabe926f" BlockName="_MA_Buy1" Name="MAType" InvariantName="MAType" CodeName="_MA_Buy1_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="6baa8087-30bd-4927-aa06-2cf6a509795d" BlockName="_MA_Buy2" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Buy2_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="10" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="6baa8087-30bd-4927-aa06-2cf6a509795d" BlockName="_MA_Buy2" Name="MAType" InvariantName="MAType" CodeName="_MA_Buy2_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="a03f3ede-ad45-428a-a7d4-bf89f84663f8" BlockName="_MA_Sell_2" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Sell_2_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="10" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="a03f3ede-ad45-428a-a7d4-bf89f84663f8" BlockName="_MA_Sell_2" Name="MAType" InvariantName="MAType" CodeName="_MA_Sell_2_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
    </Parameters>""",
                               f"""<Sources>
      <Source DataSourceName="BinanceFutures" SecurityId="{i[0]}" Name="13E828E4-4633-455C-B81B-730B003D8002" VisualTypeName="Торгуемый инструмент" IsOption="false">
        <Records />
      </Source>
      <Source DataSourceName="BinanceFutures" SecurityId="{i[1]}" Name="dae2c52a-3337-4eea-9caf-f302f70848d5" VisualTypeName="Торгуемый инструмент" IsOption="false">
        <Records />
      </Source>
    </Sources>
    <Parameters>
      <Parameter xsi:type="OptimData" ItemName="4a074d54-81cb-4469-bbd7-698000095100" BlockName="НачальныйBuy1" Name="Значение" InvariantName="Value" CodeName="НачальныйBuy1_Value" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelbuy1']['Dev']}" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="c149f466-7e54-4b9f-b86a-ca97cdda67be" BlockName="НачальныйSell1" Name="Значение" InvariantName="Value" CodeName="НачальныйSell1_Value" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelsell1']['Dev']}" TypeName="Double" MinValue="0" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="3ecf4a44-b37b-4080-9acf-3c19e06d771a" BlockName="НачальныйBuy2" Name="Значение" InvariantName="Value" CodeName="НачальныйBuy2_Value" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelbuy2']['Dev']}" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="104fa729-feab-466a-baed-7a94e61b1417" BlockName="НачальныйSell2" Name="Значение" InvariantName="Value" CodeName="НачальныйSell2_Value" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelsell2']['Dev']}" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="IntOptimData" ItemName="5123f484-6315-489f-8063-59b75593c17f" BlockName="_MA_Sell_1" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Sell_1_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelsell1']['MA Period']}" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="5123f484-6315-489f-8063-59b75593c17f" BlockName="_MA_Sell_1" Name="MAType" InvariantName="MAType" CodeName="_MA_Sell_1_MAType" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelsell1']['MA Type']}" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="2f3a13c8-9c42-4cac-90ed-36a8aabe926f" BlockName="_MA_Buy1" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Buy1_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelbuy1']['MA Period']}" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="2f3a13c8-9c42-4cac-90ed-36a8aabe926f" BlockName="_MA_Buy1" Name="MAType" InvariantName="MAType" CodeName="_MA_Buy1_MAType" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelbuy1']['MA Type']}" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="6baa8087-30bd-4927-aa06-2cf6a509795d" BlockName="_MA_Buy2" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Buy2_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelbuy2']['MA Period']}" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="6baa8087-30bd-4927-aa06-2cf6a509795d" BlockName="_MA_Buy2" Name="MAType" InvariantName="MAType" CodeName="_MA_Buy2_MAType" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelbuy2']['MA Type']}" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="a03f3ede-ad45-428a-a7d4-bf89f84663f8" BlockName="_MA_Sell_2" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Sell_2_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelsell2']['MA Period']}" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="a03f3ede-ad45-428a-a7d4-bf89f84663f8" BlockName="_MA_Sell_2" Name="MAType" InvariantName="MAType" CodeName="_MA_Sell_2_MAType" UsedInOptimization="false" IsCalculable="false" Value="{param['Levelsell2']['MA Type']}" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
    </Parameters>""")
    replace_setting = setting_agent.replace(
        """Name":"13E828E4-4633-455C-B81B-730B003D8002","VisualTypeName":"Торгуемый инструмент","IsOption":false,"Records":[],"DataSourceName":"BinanceFutures","SecurityId":"CELRUSDT","IsDefined":true""",
        f"""Name":"13E828E4-4633-455C-B81B-730B003D8002","VisualTypeName":"Торгуемый инструмент","IsOption":false,"Records":[],"DataSourceName":"BinanceFutures","SecurityId":"{i[0]}","IsDefined":true""")
    replace_setting = replace_setting.replace(
        """Name":"dae2c52a-3337-4eea-9caf-f302f70848d5","VisualTypeName":"Торгуемый инструмент","IsOption":false,"Records":[],"DataSourceName":"BinanceFutures","SecurityId":"ONEUSDT","IsDefined":true""",
        f"""Name":"dae2c52a-3337-4eea-9caf-f302f70848d5","VisualTypeName":"Торгуемый инструмент","IsOption":false,"Records":[],"DataSourceName":"BinanceFutures","SecurityId":"{i[1]}","IsDefined":true""")
    max_cand = []
    max_cand.append(param['Levelbuy1']['MA Period'])
    max_cand.append(param['Levelbuy2']['MA Period'])
    max_cand.append(param['Levelsell1']['MA Period'])
    max_cand.append(param['Levelsell2']['MA Period'])
    max_cand = max(max_cand) + 20
    replacecode = replacecode.replace("""<MaxCandels>100</MaxCandels>""", f"""<MaxCandels>{max_cand}</MaxCandels>""")
    uid = str(uuid.uuid4())
    date_st = "2002-02-20 02:20:02"
    date_end = "2002-02-20 02:20:02"
    params_script = (id_script, uid, name_pair, replacecode, setting_script, config.ma_type[ma_num], date_st, date_end)
    sql_select_query_script = '''INSERT INTO Script VALUES(?, ?,?,?,0,NULL ,?, ?,'<tags />',0,?,?,572 )'''
    c.execute(sql_select_query_script, params_script)
    params_agent = (
        id_agent, 1, 0, 0, 0, replace_setting, 'Script', id_script)
    sql_select_query_agent = '''INSERT INTO Agent VALUES(?,NULL,NULL,?,?,?,?,?,NULL,?,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,?)'''
    c.execute(sql_select_query_agent, params_agent)
    extend = """<?xml version="1.0" encoding="utf-16"?>
<XmlExtendRecords xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <Records />
</XmlExtendRecords>"""
    params_map1 = (
        id_map, '13E828E4-4633-455C-B81B-730B003D8002', i[0], extend, id_agent, portfolio_id)
    sql_select_query_map1 = '''INSERT INTO Mapping VALUES(?,?,?,NULL,?,?,'TradeMapping',NULL,?)'''
    c.execute(sql_select_query_map1, params_map1)
    id_map += 1
    params_map2 = (
        id_map, 'dae2c52a-3337-4eea-9caf-f302f70848d5', i[1], extend, id_agent,portfolio_id)
    sql_select_query_map2 = '''INSERT INTO Mapping VALUES(?,?,?,NULL,?,?,'TradeMapping',NULL,?)'''
    c.execute(sql_select_query_map2, params_map2)
    params_agent_event = (
        id_ag_ev, 0)
    sql_select_query_ag_ev = '''INSERT INTO AgentEvent VALUES(?,0,'2021-06-29 06:36:05.3566736',?)'''
    c.execute(sql_select_query_ag_ev, params_agent_event)
    id_agent += 1
    id_script += 1
    id_map += 1
    id_ag_ev += 1
    conn.commit()
conn.close()
