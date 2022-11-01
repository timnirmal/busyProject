# for each file in a directory, read the file and write the contents to a single file

import os
import glob
import pandas as pd

# get the current working directory
cwd = os.getcwd()

print(cwd)

# get all files in the directory
files = glob.glob("../CSV2" + "/*.csv")


# create a list to hold the contents of all files
all_files = []



# loop through all files
for filename in files:
    # read the content of the file and append to the list
    df = pd.read_csv(filename, index_col=None, header=0)
    # convert dataframe to string
    df_string = df.to_string()
    # write the string to a file
    with open("allData.txt", "a") as f:
        f.write(df_string)
        f.write("\n\n\n\n")








"""
/**
* This will add all content into one dataframe csv
"""
# loop through all files
# for filename in files:
#     # read the content of the file and append to the list
#     df = pd.read_csv(filename, index_col=None, header=0)
#     all_files.append(df)


# # concatenate all files in the list
# data_frame = pd.concat(all_files, axis=0, ignore_index=True)
#
# # write the content to a single file
# data_frame.to_csv("all_data.csv", index=False)
#
# # read the content of the single file
# df = pd.read_csv("all_data.csv")
#
# # print the content of the single file
# print(df)

