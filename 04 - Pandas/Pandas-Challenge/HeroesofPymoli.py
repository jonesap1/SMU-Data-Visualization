# Dependencies & Starting Data
import pandas as pd
import numpy as np

pymoli_data_file="Resources/purchase_data.csv"

#Initial Data Frame read to make sure file is working
pymoli_df=pd.read_csv(pymoli_data_file)
pymoli_df.head()

#Total Number of Players
uniqueplayers = pymoli_df["SN"].unique()
totplayers=len(uniqueplayers)

#Unique Items
uniqueitemname=pymoli_df["Item Name"].unique()
totitems=len(uniqueitemname)

#Average Price
avgprice=pymoli_df["Price"].mean()
avgpricecurrency="${:,.2f}".format(avgprice)
avgpricecurrency

#Total #Purchases
totalpurchase=pymoli_df["Purchase ID"].count()
totalpurchase

#Total Revenue
totalrevenue=pymoli_df["Price"].sum()
totalrevenue="${:,.2f}".format(totalrevenue)
totalrevenue

summary_df=pd.DataFrame({"Total Players":[totplayers],"Total Unique Items":[totitems],
                    "Average Purchase Price":[avgpricecurrency],"Total Purchases":[totalpurchase],"Total Revenue":[totalrevenue]})
summary_df

#GENDER DEMOGRAPHICS

#only count unique screen names
gender_df=pymoli_df[["SN","Gender"]].drop_duplicates(keep='first')
#check for correctness unique sn = unique players
gender_df
#Total Gender Stats
genderstats=gender_df["Gender"].value_counts()
genderstats

#male players

maleplayers=gender_df[gender_df["Gender"]=="Male"].count()
maleplayers

#Percent Players
percentmale=maleplayers/totplayers
percentmale