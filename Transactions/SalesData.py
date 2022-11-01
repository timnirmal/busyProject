from datetime import datetime

from supabase import create_client
import uuid
import json
import pandas as pd

API_URL = 'https://qemtgmilflgbhgrhnmdx.supabase.co'
API_KEY = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InFlbXRnbWlsZmxnYmhncmhubWR4Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTY2NjI0ODUyOCwiZXhwIjoxOTgxODI0NTI4fQ.E9ZkTW2dKolRSTjMSlAbFBbkbbKf-huq8WAzzOy5GlM'
supabase = create_client(API_URL, API_KEY)
print(supabase)

# show all columns in df head
pd.set_option('display.max_columns', None)


def getTran1Data(id: int, columnlist: list):
    # Select all rows from sales_order where id = id, include 'PO'
    # response = supabase.table('tran1').select('*').eq('companyid', id).like('vchno', '%PO%').limit(5).execute()
    response = supabase.table('tran1').select('*').eq('companyid', id).like('vchno', '%PO%').execute()
    # Convert response to dataframe
    df = pd.DataFrame(response.data)
    # remove columns from df
    # df.drop(['id','companyid','created_at','updated_at','deleted_at'], axis=1, inplace=True)
    # only keep columnList columns in df
    df = df[columnlist]
    return df


def getMasterFootPrintData(id: int, columnlist: list):
    if columnlist == None:
        columnlist = ["mastercode", "name", "mastertype"]

    # Select all rows from sales_order where id = id, include 'PO'
    response = supabase.table('mastfootprint').select(ConvertListToStr(columnlist)).eq('companyid', id).execute()
    # Convert response to dataframe
    df = pd.DataFrame(response.data)
    # sort df by mastercode
    df.sort_values(by=['mastercode'], inplace=True)

    return df


def getTran2Data(id: int, columnlist: list):
    if columnlist == None:
        columnlist = ["mastercode", "name", "mastertype", "value1", "value2", "value3"]

    # Select all rows from sales_order where id = id, include 'PO'
    response = supabase.table('tran2').select(ConvertListToStr(columnlist)).eq('companyid', id).like('vchno',
                                                                                                     '%PO%').execute()
    # Convert response to dataframe
    df = pd.DataFrame(response.data)
    # sort df by mastercode
    df.sort_values(by=['vchno'], inplace=True)

    # df['value1'] to absolute value
    df['value1'] = df['value1'].abs()
    df['value2'] = df['value2'].abs()


    return df


def getMaster1Data(id: int, columnlist: list):
    if columnlist == None:
        columnlist = ["code", "name", "mastertype"]

    # Select all rows from sales_order where id = id, include 'PO'
    response = supabase.table('master1').select(ConvertListToStr(columnlist)).eq('companyid', id).execute()
    # Convert response to dataframe
    df = pd.DataFrame(response.data)
    # sort df by mastercode
    df.sort_values(by=['code'], inplace=True)

    return df


# id: int and columnlist: list
def Sales_Order(id: int, tran1ColumnList=None, master1ColumnList=None, tran2ColumnList=None,
                masterFootPrintColumnList=None):
    # Date, PO, Customer, Item, Qty, Unit, Price, Amount
    if tran1ColumnList is None:
        tran1ColumnList = ["date", "vchcode", "vchno", "mastercode1", "mastercode2"]

    if masterFootPrintColumnList is None:
        masterFootPrintColumnList = ["mastercode", "name", "mastertype"]

    if master1ColumnList is None:
        master1ColumnList = ["code", "name", "mastertype"]

    if tran2ColumnList is None:
        tran2ColumnList = ["vchcode", "mastercode2", "srno", "mastercode1", "rectype", "vchtype", "vchno", "value1",
                           "value2", "value3"]

    # calcualte time difference between below for loop
    timeNow = datetime.now()

    df = getTran1Data(id, tran1ColumnList)
    dfMasterFootPrint = getMasterFootPrintData(id, masterFootPrintColumnList)
    dfTran2 = getTran2Data(id, tran2ColumnList)
    dfMaster1 = getMaster1Data(id, master1ColumnList)

    # create a new column in df called 'mastercode1', 'name', 'mastertype', 'itemcode', 'itemname', 'qty', ''
    df['mastercode2'] = ""
    df['name'] = ""
    df['mastertype'] = ""

    df["vchno2"] = ""
    df['itemcode'] = ""
    df['itemname'] = ""
    df['qty'] = ""
    df['price'] = ""
    df['amount'] = ""


    print(df)
    print()
    print()
    print(dfMasterFootPrint)
    print()
    print()
    print(dfTran2)

    # save df to csv
    df.to_csv("Sales_Order.csv", index=False)

    # save dfMasterFootPrint to csv
    dfMasterFootPrint.to_csv("Master.csv", index=False)

    # save dfTran2 to csv
    dfTran2.to_csv("Tran2.csv", index=False)

    # save dfMaster1 to csv
    dfMaster1.to_csv("Master1.csv", index=False)

    """
    *
    ** Now we have All the data needed.
    
    1. Get Data from Tran1
    2. Find User Name from MasterFootPrint
    3. Find Items from Tran2
    4. Replace Tran2 data with Master1 data (Item Name)
    """

    """
    2. Find User Name from MasterFootPrint
    """

    # for each row in df
    for index, row in df.iterrows():
        masterCode = row.mastercode1
        # find the row in dfMasterFootPrint where mastercode = masterCode and get the name
        name = dfMasterFootPrint.loc[dfMasterFootPrint['mastercode'] == masterCode, 'name'].iloc[0]
        # find the row in dfMasterFootPrint where mastercode = masterCode and get the mastertype
        mastertype = dfMasterFootPrint.loc[dfMasterFootPrint['mastercode'] == masterCode, 'mastertype'].iloc[0]
        # set the name and mastertype in df
        df.at[index, 'name'] = name
        df.at[index, 'mastertype'] = mastertype
        # set mastercode
        df.at[index, 'mastercode2'] = masterCode

    print("After adding MasterFootPrint data")
    print("After adding MasterFootPrint data")
    print("After adding MasterFootPrint data")
    print(df)

    # save df to csv
    df.to_csv("Sales_Order_New.csv", index=False)

    # Now df have date,vchcode,vchno,mastercode1,mastercode2,name,mastertype columns

    """
    3. Find name of each master code of Items
    Tran2 mastercode1 merge with MasterFootPrint mastercode
    """
    # for each row in df
    for index, row in dfTran2.iterrows():
        masterCode = row.mastercode1
        # find the row in dfMasterFootPrint where mastercode = masterCode and get the name
        name = dfMasterFootPrint.loc[dfMasterFootPrint['mastercode'] == masterCode, 'name'].iloc[0]
        # find the row in dfMasterFootPrint where mastercode = masterCode and get the mastertype
        mastertype = dfMasterFootPrint.loc[dfMasterFootPrint['mastercode'] == masterCode, 'mastertype'].iloc[0]
        # set the name and mastertype in df
        dfTran2.at[index, 'itemname'] = name
        dfTran2.at[index, 'mastertypeitem'] = mastertype
        # set mastercode
        dfTran2.at[index, 'mastercode2'] = masterCode

    print("After adding MasterFootPrint data")
    print("After adding MasterFootPrint data")
    print("After adding MasterFootPrint data")
    print(dfTran2)

    # save df to csv
    dfTran2.to_csv("Sales_Order_New_Tran2.csv", index=False)


    """
    4. Find Items from Tran2
    """

    # for each row in dfTran2
    # vchcode - 24
    # mastercode2 - 1255
    # srno - 4
    # mastercode1 - 1255
    # rectype - 4
    # vchtype - 13
    # vchno - PO-1
    # value1 - 5
    # value2 - 5000
    # value3 - 27500
    # itemname - R/M Ginger Flavour
    # mastertype - 6.0 (item)


    # inlcude
    # date
    # name
    # mastertype

    # for each row in df
    for index, row in dfTran2.iterrows():
        vchno = row.vchno
        # find the row in DfTran2 where vchno = vchno
        dfTemp = df.loc[df['vchno'] == vchno]

        print("Df Temp")
        print(dfTemp)
        print()
        print()

        # if dfTemp is not empty
        if not dfTemp.empty:
            # count number of rows in dfTemp
            count = dfTemp.shape[0]
            # for each row in dfTemp
            for index2, row2 in dfTemp.iterrows():
                # add new row to df with same data as df
                dfTran2 = dfTran2.append(row, ignore_index=True)

                print("Row 2")
                print(row2)
                # vchcode                             7858
                # mastercode2                         1222
                # srno                                   2
                # mastercode1                         1222
                # rectype                                4
                # vchtype                               13
                # vchno                             PO-151
                # value1                             22000
                # value2                           22000.0
                # value3                           49940.0
                # name           P/M Bottle Lid 28MM Brown
                # mastertype                           6.0

                # set the itemcode, itemname, qty in df
                dfTran2.at[index + index2, 'vchno2'] = row2.vchno
                dfTran2.at[index + index2, 'itemcode'] = row2.mastercode1
                dfTran2.at[index + index2, 'qty'] = row2.value1
                dfTran2.at[index + index2, 'price'] = row2.value2
                dfTran2.at[index + index2, 'amount'] = row2.value3
                dfTran2.at[index + index2, 'itemname'] = row2.itemname

    # sort df by vchno
    df.sort_values(by=['vchno'], inplace=True)

    # # get the name and mastertype from dfMasterRow
    # name = dfMasterRow.iloc[0]['name']
    # mastertype = dfMasterRow.iloc[0]['mastertype']
    # # set the name and mastertype in df
    # df.at[index, 'name'] = name
    # df.at[index, 'mastertype'] = mastertype

    print("Final")
    print("Final")
    print("Final")
    print(df)

    # save df to csv
    df.to_csv("Sales_Order_Final.csv", index=False)

    """
    4. Prepare Items table
    """

    # for each row in df print the row
    for index, row in df.iterrows():
        mastercode = row.mastercode1
        # response = supabase.table('mastfootprint').select(ConvertListToStr(master1ColumnList)).eq('companyid', id).eq('mastercode',
        #                                                                                                             mastercode).execute()

        # find mastercode in dfMasterFootPrint
        dfMasterRow = dfMasterFootPrint.loc[dfMasterFootPrint['mastercode'] == mastercode]

        # if mastercode is found in dfMasterFootPrint
        if not dfMasterRow.empty:
            # add name and mastertype to df
            df.at[index, 'name'] = dfMasterRow.iloc[0].name
            df.at[index, 'mastertype'] = dfMasterRow.iloc[0].mastertype

        # print(df)

    timeNew = datetime.now()
    # print timeNew - timeNow converted to minutes
    print()
    print()
    print((timeNew - timeNow).total_seconds())

    SalesOrders = df.to_json(orient="records", indent=4, date_format='iso', date_unit='s')

    # Convert json to dict
    SalesOrders = json.loads(SalesOrders)

    # print(SalesOrders)

    return SalesOrders


def ConvertListToStr(columnList):
    return str(columnList).replace("[", "").replace("]", "").replace("'", '"')


def main():
    print("Hello World")
