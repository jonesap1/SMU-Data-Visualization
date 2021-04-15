#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 23:37:09 2021

@author: imacpro
"""

import pandas as pd
election_data_file = "Resources/election_data.csv"

election_data_df = pd.read_csv(election_data_file)
#election_data_df.head()

#Total number of votes
totalvotes = election_data_df["Voter ID"].count()
#print("📨TOTAL BALOTS CAST",totalvotes)

#canidates
#print(election_data_df["Candidate"].unique())
election_data_df["Candidate"].unique()

#add voter counts
countvotes = 1
election_data_df["Voter Count"] = countvotes
#print(election_data_df.head())

#group canidates and vote count

results_df = election_data_df[["Candidate", "Voter Count"]].groupby(["Candidate"])
groupedresults_df = results_df.sum()
#print("🧾 ELECTION SUMMARY",groupedresults_df)

#% of Votes
canvotepercent_df = groupedresults_df["Voter Count"]/totalvotes
#print(canvotepercent_df)

groupedresults_df["% OF VOTES"] = canvotepercent_df
#percentformat = {'% OF VOTES':'{:.2%}'}
#groupedresults_df.style.format(percentformat)
groupedresults_df["% OF VOTES"] = groupedresults_df["% OF VOTES"].map("{:.2%}".format)
print(groupedresults_df)

popvote = groupedresults_df['Voter Count'].max()
#print("🗳POPULAR VOTE",popvote)


winner=(groupedresults_df["Voter Count"]==popvote)

candidate = groupedresults_df[winner]
#print("CONGRATULATIONS TO THE WINNER:",candidate.index[0])

#summary_df = pd.DataFrame({"📨TOTAL BALOTS CAST": [totalvotes],\
#                            "🧾 ELECTION SUMMARY": groupedresults_df})
#summary = str(f'ELECTION RESULTS\n--------------------\nTOTAL BALOTS CAST: {totalvotes}\n--------------------------\nELECTION SUMMARY\n{groupedresults_df.iloc[:,:]}\n-----------------------\nPOPULAR VOTE[popvote}\nCONGRATULATIONS{candidate.index[0]}\n-----------------------')
summary = str(f'🗳ELECTION RESULTS\n--------------------------------------\n📨TOTAL BALOTS CAST: {totalvotes}\n--------------------------------------\n🧾 ELECTION SUMMARY\n{groupedresults_df.iloc[:,:]}\n--------------------------------------\n🎉CONGRATULATIONS TO THE WINNER: {candidate.index[0]}\n--------------------------------------\n🗳POPULAR VOTE: {popvote}')
fileout = open("../PyPoll/output/newpoll.txt","w") 
fileout.write(summary)
print(summary)




malegamers=gender_df[gender_df["Gender"]=='Male'].count()
malegamers

permalegamer=malegamers/totplayers
femalegamers=gender_df.loc[gender_df["Gender"]=='Female'].count()
femalegamers
perfemalegamer=femalegamers/totplayers
othergamers=gender_df.loc[gender_df["Gender"]=='Other / Non-Disclosed'].count()
othergamers
perothergamer=othergamers/totplayers
gendersummary_df=pd.DataFrame({"Gender":["Male","Female","Other / Non-Disclosed"],"Total":[malegamers[0],femalegamers[0],othergamers[0]],"Percentage of Total Players":[permalegamer[0],perfemalegamer[0],perothergamer[0]]})
print(gendersummary_df)
gendersummary_df["Percentage of Total Players"] = gendersummary_df["Percentage of Total Players"].map("{:.2%}".format)
gendersummary_df.set_index("Gender")
gendersummary_df

#percent_format={'Percentage of Total Players':'{:.2%}'}