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
print(totalvotes)

#canidates
#print(election_data_df["Candidate"].unique())
election_data_df["Candidate"].unique()

#add voter counts
countvotes = 1
election_data_df["Voter Count"] = countvotes
print(election_data_df.head())

#group canidates and vote count

results_df = election_data_df[["Candidate", "Voter Count"]].groupby(["Candidate"])
comparison_df = results_df.sum()

print(comparison_df)

#% of Votes
candidateper = comparison_df["Voter Count"]/totalvotes
print(candidateper)

candidate

candidateperper = (comparison_df)