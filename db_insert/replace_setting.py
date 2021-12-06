import sqlite3

conn = sqlite3.connect('D:\TSLab.sqlite')
cursor = conn.cursor()
sql_select_query = """SELECT * FROM Script WHERE ParentId = ?"""
cursor.execute(sql_select_query, (1125,))
records = cursor.fetchall()
for row in records:
    id = row[1]
    print(id)
    setting = str(row[3]).replace('<RecalcInterval>INTERVAL</RecalcInterval>',
                                  '<RecalcInterval>BIDASK_NO_VOLUME</RecalcInterval>')
    sql = """UPDATE Script SET Code = ? WHERE UniqueId = ?"""
    cursor.execute(sql, (setting, id))
conn.commit()
