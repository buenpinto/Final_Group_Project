#Some imports
import pandas as pd
import numpy  as np
from matplotlib import pyplot as plt
import matplotlib.dates as dates
import os
############## Data imports and variable renames (for consistency) #############

casen2006 = pd.read_csv("CASEN_2006.csv", usecols=["seg", "f", "o","pobreza_mn", "ypchmonecor", "ypchtotcor"])

casen2006.rename(columns={"ypchmonecor":"monetary_income_2006", "ypchtotcor":"total_income_2006"}, inplace = True)


casen2009 = pd.read_csv("CASEN_2009.csv", usecols=["segmento", "idviv", "o","pobreza_mn", "ypchmonecor", "ypchtotcor"])

casen2009.rename(columns={'segmento':'seg', "idviv":"f", "ypchmonecor":"monetary_income_2009",
"ypchtotcor":"total_income_2009"}, inplace = True)



casen2011 = pd.read_csv("CASEN_2011.csv", usecols=["folio", "o","pobreza_mn", "ypchmonecor", "ypchtotcor"])

casen2011.rename(columns={'folio':'seg', "ypchmonecor":"monetary_income_2011", "ypchtotcor":"total_income_2011"}, inplace = True)



casen2013 = pd.read_csv("CASEN_2013.csv", usecols=["folio", "o", "pobreza_mn", "ymonecorh", "ypchtot",])

casen2013.rename(columns={'folio':'seg', "ymonecorh":"monetary_income_2013","ypchtot":"total_income_2013"}, inplace = True)


################################### 2006 #######################################

# Casen 2006

#casen2006 = casen2006.sort_values(by = "seg")
#Converts the int columns into string values
casen2006["seg"]=casen2006["seg"].astype(str)

# We get the substring that identifies counties in the data base, and create a
# new column with it
casen2006["Comuna_ID"]=casen2006["seg"].apply(lambda x: x[:4] if len(x)== 7 else x[:5])
casen2006["Region_ID"]=casen2006["seg"].apply(lambda x: x[:1] if len(x)== 7 else x[:2])

#Looking at the data base
#comuna_2006=round(casen2006.groupby("Comuna_ID")[["ypchtotcor"]].mean().sort_values(by ="ypchtotcor"),2)
#region_2006=round(casen2006.groupby("Region_ID")[["ypchtotcor"]].mean().sort_values(by ="ypchtotcor"),2)


# Regions 14 and 15 are newer Regions, created after 2006:
#print(casen2006["pobreza_mn"])

#Generating the some dummy variables with the data:

casen2006["extreme_poverty_2006"] = casen2006["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2006["poverty_2006"] = casen2006["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2006["no_poverty_2006"] = casen2006["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)



#print(casen2006[["extreme_poverty","poverty", "no_poverty", "pobreza_mn"]])

# Grouping thr data at a comuna level:

casen2006_com = casen2006.groupby("Comuna_ID")[["extreme_poverty_2006", "poverty_2006", "no_poverty_2006",
"monetary_income_2006","total_income_2006"]].mean()

#print(casen2006_com)

################################### 2009 #######################################

# Casen 2009

casen2009 = casen2009.sort_values(by = "seg")

casen2009["seg"]=casen2009["seg"].astype(str)

casen2009["Comuna_ID"]=casen2009["seg"].apply(lambda x: x[:4] if len(x)== 7 else x[:5])
casen2009["Region_ID"]=casen2009["seg"].apply(lambda x: x[:1] if len(x)== 7 else x[:2])


#Generating the some dummy variables with the data:

casen2009["extreme_poverty_2009"] = casen2009["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2009["poverty_2009"] = casen2009["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2009["no_poverty_2009"] = casen2009["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)

# Grouping thr data at a comuna level:

casen2009_com = casen2009.groupby("Comuna_ID")[["extreme_poverty_2009", "poverty_2009", "no_poverty_2009",
"monetary_income_2009","total_income_2009"]].mean()


#print(casen2009_com)


################################### 2011 #######################################

#casen2011

casen2011 = casen2011.sort_values(by = "seg")

casen2011["seg"]=casen2011["seg"].astype(str)

casen2011["Comuna_ID"]=casen2011["seg"].apply(lambda x: x[:4] if len(x)== 11 else x[:5])
casen2011["Region_ID"]=casen2011["seg"].apply(lambda x: x[:1] if len(x)== 11 else x[:2])

#Generating the some dummy variables with the data:

casen2011["extreme_poverty_2011"] = casen2011["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2011["poverty_2011"] = casen2011["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2011["no_poverty_2011"] = casen2011["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)


# Grouping the data at a comuna level:

casen2011_com = casen2011.groupby("Comuna_ID")[["extreme_poverty_2011", "poverty_2011", "no_poverty_2011",
"monetary_income_2011","total_income_2011"]].mean()




################################### 2013 #######################################

#casen2013

casen2013 = casen2013.sort_values(by = "seg")

casen2013["seg"]=casen2013["seg"].astype(str)

casen2013["Comuna_ID"]=casen2013["seg"].apply(lambda x: x[:4] if len(x)== 11 else x[:5])
casen2013["Region_ID"]=casen2013["seg"].apply(lambda x: x[:1] if len(x)== 11 else x[:2])

#Generating the some dummy variables with the data:

casen2013["extreme_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2013["poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2013["no_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)

# Grouping the data at a comuna level:

casen2013_com = casen2013.groupby("Comuna_ID")[["extreme_poverty_2013", "poverty_2013", "no_poverty_2013",
"monetary_income_2013","total_income_2013"]].mean()

#print(casen2006_com.head(5))
#print(casen2009_com.head(5))

######################## The data merging ######################################

merged1 =casen2006_com.join(casen2009_com)

merged2 = merged1.join(casen2011_com)

Casen_ALL_com = merged2.join(casen2013_com)

#print(Casen_ALL_com)

#Drop counties that have missing values (changed name, code, region, data quality, etc. )
# We still have 301/360 counties with information for the 4 years
Casen_ALL_com.dropna(inplace = True)


#################### PASTE COUNTY NAMES #######################################


cod_com = pd.read_csv("COUNTY_CODES.csv", usecols= ["region", "comuna", "zona", "comuna_name"],
sep=",", encoding='latin-1', index_col="comuna")

cod_com.rename(columns={"comuna":"Comuna_ID", "zona":"Zone", "comuna_name":"county_name"}, inplace = True)

cod_com.index.rename("Comuna_ID", inplace = True)

#Set the index to int64 format
Casen_ALL_com.index=Casen_ALL_com.index.astype('int')

#print(cod_com.index)
#print(Casen_ALL_com.index)

Casen_ALL_com = Casen_ALL_com.join(cod_com)

#print(Casen_ALL_com[["extreme_poverty_2006","county_name"]])

#export the file
Casen_ALL_com.to_csv("Casen_all_final.csv")
