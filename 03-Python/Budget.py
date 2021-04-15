# -*- coding: utf-8 -*-
"Code to analyze Budget Data"

# LIBRARIES
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import datetime

#LOAD RAW DATA
print("FINANCIAL ANALYSIS")
print("______________________________________")
raw_data = "Resources/budget_data.csv"
bank_raw_df = pd.read_csv(raw_data)
#print(bank_raw_df.head())

# Total Number of Months in file
#print(bank_raw.count())
#print(bank_raw)
#total_months = bank_raw.count()-1
#print(total_months)

bank_rows = len(bank_raw_df["Date"].unique())-1
print('📆Total Months: ',bank_rows)


# NET PROFIT/LOSSES"
#bank_raw_df["Profit/Losses"] = bank_raw_df["Profit/Losses"].map("${:.2f}".format)
#bank_raw_df["Profit/Losses"] = bank_raw_df["Profit/Losses"].astype(float).map("${:,.2f}".format)
#bank_raw_df.loc[:,"Profit/Losses"]=bank_raw_df["Profit/Losses"].astype("float")
bank_raw_df.dtypes
#total_profloss = sum(bank_raw_df['Profit/Losses'])
total_profloss = bank_raw_df["Profit/Losses"].sum()
currency_profloss="${:,.2f}".format(total_profloss)
print('💰TOTAL: $', currency_profloss)

#CHANGES IN PROFIT LOSS OER THE PERIOD  
#total_changes = bank_raw_df["Profit/Losses"].mean()
avg_changes = bank_raw_df["Profit/Losses"].diff(periods=1)
bank_raw_df['Daily Change'] = avg_changes
total_changes = bank_raw_df["Daily Change"].mean()
currency_changes="${:,.2f}".format(total_changes)
print('💸 AVERAGE CHANGE: ',currency_changes)


#MAX & MIN CHANGE BY DATE
changemax = bank_raw_df["Daily Change"].max()
#bankdate_df= bank_raw_df.loc[bank_raw_df["Daily Change"] == changemax,:]
maxdate = (bank_raw_df["Daily Change"] == changemax)
maxmonth = bank_raw_df[maxdate].Date.values[0]
#print(maxmonth)
currency_changemax="${:,.2f}".format(changemax)
print("🔺GREATEST INCREASE IN PROFITS: ",maxmonth, currency_changemax)


changemin = bank_raw_df["Daily Change"].min()
#mindate_df= bank_raw_df.loc[bank_raw_df["Daily Change"] == changemin,:]
mindate = (bank_raw_df["Daily Change"] == changemin)
minmonth = bank_raw_df[mindate].Date.values[0]
currency_changemin="${:,.2f}".format(changemin)
print("🔻GREATEST DECREASE IN PROFITS: ",minmonth, currency_changemin)
#print(minmonth)

      
   

#bank_raw_df=bank_raw_df.sort_values("Daily Change")
#bank_raw_df=bank_raw_df.reset_index(drop=True)
#print(bank_raw_df)

#print(bankdate_df.head())
#print(changemin)

#datemax = bank_raw_df["Daily Change"] == changemax
#datemin= bank_raw_df["Daily Change"] == changemin

#print("GREATEST INCREASE IN PROFITS: ",datemax)
#d = datetime.datetime.strptime('Dec 2016','%b %Y').strftime('%d/%m/%Y')
#print(datetime.strftime(datetime.strptime(s, '%b %Y'), '%d/%m/%Y'))
   
#PRINT SUMMARY ANALYSIS
#summary = summary{f'FINANCIAL ANALYSIS\n________________________\n
                 # "Total Months": {lenbank_rows], "Total Profit/Losses": [total_profloss]}
#summary_df=pd.DataFrame(data=summary)
#summary_df.head()




