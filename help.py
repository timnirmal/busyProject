import os
from pathlib import Path
import pandas as pd
import time

import pyodbc as pyodbc

newpath = r'C:\BusyWin\DATA\upload'
if not os.path.exists(newpath):
    os.makedirs(newpath)

# copy file to new location
import shutil
import pypyodbc

# check if file exists
if os.path.isfile(r'C:\BusyWin\DATA\upload\db.accdb'):
    print("File exists.")
else:
    shutil.copyfile(r'C:\BusyWin\DATA\db.bds', r'C:\BusyWin\DATA\upload\db.bds')
    p = Path(r'C:\BusyWin\DATA\upload\db.bds')
    p.rename(p.with_suffix('.accdb'))

# wait 2 seconds
time.sleep(2)

pypyodbc.lowercase = False
print("Connecting to database...")
print([x for x in pyodbc.drivers()])
# conn = pypyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\BusyWin\DATA\upload\db.accdb;')

MDB = 'C:\\BusyWin\\DATA\\upload\\db.accdb'
DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
PASSWORD = 'ILoveMyINDIA'
conn = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV, MDB, PASSWORD))

print("Connected to database.")
cur = conn.cursor()
cur.execute("SELECT * FROM Company")
print("Company table:")
for row in cur.fetchall():
    print(row)

# All columns in dataframe
pd.set_option('display.max_columns', None)

print("All Tables:")
# cur.execute("SELECT * FROM MSysObjects WHERE Type=1")
# for row in cur.fetchall():
#     print(row)
for row in cur.tables():
    # print(row)
    # print(row.table_name)
    if row.table_type == 'TABLE':
        print(row)

        # create pandas dataframe from table
        df = pd.read_sql("SELECT * FROM " + row.table_name, conn)
        print("Dataframe from table:")
        print(row.table_name)
        print(df)

print("All Columns:")
for col in cur.columns():
    print(col)




# while True:
#     row = cur.fetchone()
#     print(row)
#     if row is None:
#         break

cur.close()
conn.close()
