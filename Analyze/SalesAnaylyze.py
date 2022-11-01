# read csv to dataframe

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# print all columns in dataframe
pd.set_option('display.max_columns', None)

# 1. read csv to dataframe
df = pd.read_csv('../CSV2/Tran1.csv')
print(df.head())

# 2. get the number of rows and columns
print(df.shape)

# 3. get the number of rows
print(df.shape[0])

# 4. get the number of columns
print(df.shape[1])

# 5. get the column names
print(df.columns)


# # 6. for each column, find CLB7-
# for col in df.columns:
#     print(df[col].str.contains('CLB7-'))


# if column VchNo contains CLB7-, then get the row
print(df[df['VchNo'].str.contains('CLB7-   1')])


# remove column with null value
df.dropna(axis=1, how='all', inplace=True)

# remove column with all 0
df = df.loc[:, (df != 0).any(axis=0)]

# save to result.csv
df[df['VchNo'].str.contains('CLB7-   1')].to_csv('result.csv')

# read result.csv
df = pd.read_csv('result.csv')

# df to string
df_string = df.to_string()

print()
print()
print()
print()
print()
print(df_string)

# switch rows and columns






