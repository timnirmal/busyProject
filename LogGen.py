import os
from pathlib import Path

import pandas as pd
import pyodbc as pyodbc

# All columns in dataframe
pd.set_option('display.max_columns', None)

path = r'C:\BusyWin\BusyWin\DATA\COMP0011'
newpath = r'\upload'


def Convert_to_Accdb(path, newpath):
    if not os.path.exists(path + newpath):
        os.makedirs(path + newpath)
    # copy file to new location
    import shutil
    import pypyodbc
    # check if file exists
    if os.path.isfile(path + newpath + r'\db.accdb'):
        print("File exists.")
    else:
        shutil.copyfile(path + r'\db.bds', path + newpath + r'\db.bds')
        p = Path(path + newpath + r'\db.bds')
        p.rename(p.with_suffix('.accdb'))


def Connect_to_Database():
    print("Connecting to database...")
    print([x for x in pyodbc.drivers()])
    MDB = path + newpath + r'\db.accdb'
    DRV = '{Microsoft Access Driver (*.mdb, *.accdb)}'
    PASSWORD = 'ILoveMyINDIA'
    conn = pyodbc.connect('DRIVER={};DBQ={};PWD={}'.format(DRV, MDB, PASSWORD))
    print("Connected to database.")
    cur = conn.cursor()

    return cur, conn


Convert_to_Accdb(path, newpath)

cur, conn = Connect_to_Database()

# All columns in Company Database
cur.execute("SELECT * FROM Company")

print("Company table:")
for row in cur.fetchall():
    print(row)


print("All Tables:")
# cur.execute("SELECT * FROM MSysObjects WHERE Type=1")
# for row in cur.fetchall():
#     print(row)
for row in cur.tables():
    # print(row)
    # print(row.table_name)
    print()
    print()
    if row.table_type == 'TABLE':
        print(row)

        # create pandas dataframe from table
        df = pd.read_sql("SELECT * FROM " + row.table_name, conn)
        print("Dataframe from table:")
        print(row.table_name)
        print(df)

        # save dataframe to csv
        df.to_csv(r'CSV\{}.csv'.format(row.table_name), index=False)

# print("All Columns:")
# for col in cur.columns():
#     print(col)


cur.close()
conn.close()
