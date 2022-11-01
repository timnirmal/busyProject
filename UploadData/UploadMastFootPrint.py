import json

import pandas as pd
from supabase import create_client

API_URL = 'https://qemtgmilflgbhgrhnmdx.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlbXRnbWlsZmxnYmhncmhubWR4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2NjI0ODUyOCwiZXhwIjoxOTgxODI0NTI4fQ.E9ZkTW2dKolRSTjMSlAbFBbkbbKf-huq8WAzzOy5GlM'
supabase = create_client(API_URL, API_KEY)
print(supabase)

# show all columns in df head
pd.set_option('display.max_columns', None)

# open CSV2/Tran2.csv to dataframe
df = pd.read_csv("../CSV2/MastFootPrint.csv")

print(df)

# convert all column names to lowercase
df.columns = map(str.lower, df.columns)

# add companyid column to df and set to 1
df["companyid"] = 1

# convert df to json
df = df.to_json("../JSONdata/MastFootPrint.json" ,indent=4, orient="records")

# get data from json file
with open("../JSONdata/MastFootPrint.json", "r") as f:
    data = json.load(f)

print(data)

count = 0

# insert data into supabase
for row in data:
    #print(row)
    count += 1
    print(count)
    # insert row into supabase
    response = supabase.from_("mastfootprint").insert(row).execute()
    print(response)
