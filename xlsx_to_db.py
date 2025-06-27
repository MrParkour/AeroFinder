import sqlite3
import pandas as pd

cxn = sqlite3.connect('database/plane_db copy.db')
wb = pd.read_excel('database/db_excel_2.xlsx',sheet_name = 'Лист1')
wb.to_sql(name='aircrafts_2',con=cxn,if_exists='replace',index=True)
cxn.commit()
cxn.close()
