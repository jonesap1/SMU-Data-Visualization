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
#print('📆Total Months: ',bank_rows)


# NET PROFIT/LOSSES"
#bank_raw_df["Profit/Losses"] = bank_raw_df["Profit/Losses"].map("${:.2f}".format)
#bank_raw_df["Profit/Losses"] = bank_raw_df["Profit/Losses"].astype(float).map("${:,.2f}".format)
#bank_raw_df.loc[:,"Profit/Losses"]=bank_raw_df["Profit/Losses"].astype("float")
bank_raw_df.dtypes
#total_profloss = sum(bank_raw_df['Profit/Losses'])
total_profloss = bank_raw_df["Profit/Losses"].sum()
currency_profloss="${:,.2f}".format(total_profloss)
#print('💰TOTAL: ', currency_profloss)

#CHANGES IN PROFIT LOSS OER THE PERIOD
#total_changes = bank_raw_df["Profit/Losses"].mean()
avg_changes = bank_raw_df["Profit/Losses"].diff(periods=1)
bank_raw_df['Daily Change'] = avg_changes
total_changes = bank_raw_df["Daily Change"].mean()
currency_changes="${:,.2f}".format(total_changes)
#print('💸 AVERAGE CHANGE: ',currency_changes)


#MAX & MIN CHANGE BY DATE
changemax = bank_raw_df["Daily Change"].max()
#bankdate_df= bank_raw_df.loc[bank_raw_df["Daily Change"] == changemax,:]
maxdate = (bank_raw_df["Daily Change"] == changemax)
maxmonth = bank_raw_df[maxdate].Date.values[0]
#print(maxmonth)
currency_changemax="${:,.2f}".format(changemax)
#print("🔺GREATEST INCREASE IN PROFITS: ",maxmonth, currency_changemax)


changemin = bank_raw_df["Daily Change"].min()
#mindate_df= bank_raw_df.loc[bank_raw_df["Daily Change"] == changemin,:]
mindate = (bank_raw_df["Daily Change"] == changemin)
minmonth = bank_raw_df[mindate].Date.values[0]
currency_changemin="${:,.2f}".format(changemin)
#print("🔻GREATEST DECREASE IN PROFITS: ",minmonth, currency_changemin)
#print(minmonth)

      
summary = str(f'📆TOTAL MONTHS: {bank_rows}\n--------------------------------------\n💰TOTAL PROFIT/LOSSES: {currency_profloss}\n--------------------------------------\n💸 AVERAGE CHANGE: {currency_changes}\n🔺GREATEST INCREASE IN PROFITS: {maxmonth} {currency_changemax}\n--------------------------------------\n🔻GREATEST DECREASE IN PROFITS: {minmonth} {currency_changemin}\n--------------------------------------\n')
fileout = open("../PyBank/output/new.txt","w")
fileout.write(summary)
print(summary)


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
#summary_df = pd.dataframe(Summary_df{"Total Months": [bank_rows],"Total Profit/Losses": [currency_profloss], }
#summary_df=pd.DataFrame(data=summary)
#summary_df.head()
#import os
#import csv

# Specify the file to write to
#output_path = os.path.join("..","output", "new.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
#with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
#    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)

#csvwriter.writerow(['📆Total Months: ','💰TOTAL: $', '💸 AVERAGE CHANGE: ', '🔺GREATEST INCREASE IN PROFITS: ', '🔻GREATEST DECREASE IN PROFITS: '])
#data=([bank_rows,currency_profloss,currency_changes,(maxmonth + currency_changemax), (minmonth, currency_changemin )]
#csvwriter.writerow([bank_rows,currency_profloss,currency_changes,(maxmonth + currency_changemax), (minmonth, currency_changemin)])

#summary_df = pd.dataframe({rows:[data]})
#summary_df.to_csv("FinancialSummary.csv", index=False, header=True)
