#Importing pandas
import pandas as pd

#This pyton script aims to import, clean, group and then merge all four casen surveys
# that we'll be using on our time series plots. We also generate some extra
# dummy variables and county/region identifiers.

###############################################################################


#### Data imports and variable renaming (for consistency across data bases) ####

#import casen 2006 data
casen2006 = pd.read_csv("CASEN_2006.csv", usecols=["seg", "f", "o","pobreza_mn", "ypchmonecor", "ypchtotcor"])
# rename some columns
casen2006.rename(columns={"ypchmonecor":"monetary_income_2006", "ypchtotcor":"total_income_2006"}, inplace = True)

#import casen 2009 data
casen2009 = pd.read_csv("CASEN_2009.csv", usecols=["segmento", "idviv", "o","pobreza_mn", "ypchmonecor", "ypchtotcor"])
# rename some columns
casen2009.rename(columns={'segmento':'seg', "idviv":"f", "ypchmonecor":"monetary_income_2009",
"ypchtotcor":"total_income_2009"}, inplace = True)


#import casen 2011 data
casen2011 = pd.read_csv("CASEN_2011.csv", usecols=["folio", "o","pobreza_mn", "ypchmonecor", "ypchtotcor"])
# rename some columns
casen2011.rename(columns={'folio':'seg', "ypchmonecor":"monetary_income_2011", "ypchtotcor":"total_income_2011"}, inplace = True)


#import casen 2013 data
casen2013 = pd.read_csv("CASEN_2013.csv", usecols=["folio", "o", "pobreza_mn", "ymonecorh", "ypchtot",])
# rename some columns
casen2013.rename(columns={'folio':'seg', "ymonecorh":"monetary_income_2013","ypchtot":"total_income_2013"}, inplace = True)


###############################################################################

# In the folowing sections, for each Casen survey we:

# (1) Extract a unique indentifier for each county (Comuna_ID), each region (Region_ID)
# as a substring from the "seg" column.
# (2) Define some dummy variables for poverty level (We´ll use these dummies later in our django site)
# (3) Group the data at a county (Comuna_ID) level.

# We'll then merge the four surveys using the unique Comuna_ID identifier

################################### CASEN 2006 ##################################

#Converts the "seg" column from int to string values
casen2006["seg"]=casen2006["seg"].astype(str)


# We get the substring that identifies counties in the data base, and create a
# new column with it. Same with the region. Note that the Comuna_ID may be
# 4 or 5 strings long...
casen2006["Comuna_ID"]=casen2006["seg"].apply(lambda x: x[:4] if len(x)== 7 else x[:5])
casen2006["Region_ID"]=casen2006["seg"].apply(lambda x: x[:1] if len(x)== 7 else x[:2])


# Regions 14 and 15 are new administrative Regions, created after 2006,
#so we will not use them in this project.

#Generating dummy variables for 3 different poverty cathegories:
casen2006["extreme_poverty_2006"] = casen2006["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2006["poverty_2006"] = casen2006["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2006["no_poverty_2006"] = casen2006["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)


# Grouping the data at a comuna level, we keep the mean values
casen2006_com = casen2006.groupby("Comuna_ID")[["extreme_poverty_2006", "poverty_2006", "no_poverty_2006",
"monetary_income_2006","total_income_2006"]].mean()


################################### CASEN  2009 ################################


#Converts the "seg" column from int to string values
casen2009["seg"]=casen2009["seg"].astype(str)

# We get the substring that identifies counties in the data base, and create a
# new column with it. Same with the region. Note that the Comuna_ID may be
# 4 or 5 strings long...
casen2009["Comuna_ID"]=casen2009["seg"].apply(lambda x: x[:4] if len(x)== 7 else x[:5])
casen2009["Region_ID"]=casen2009["seg"].apply(lambda x: x[:1] if len(x)== 7 else x[:2])

#Generating dummy variables for 3 different poverty cathegories:
casen2009["extreme_poverty_2009"] = casen2009["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2009["poverty_2009"] = casen2009["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2009["no_poverty_2009"] = casen2009["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)


# Grouping the data at a comuna level, we keep the mean values
casen2009_com = casen2009.groupby("Comuna_ID")[["extreme_poverty_2009", "poverty_2009", "no_poverty_2009",
"monetary_income_2009","total_income_2009"]].mean()


################################### CASEN 2011 #################################


#Converts the "seg" column from int to string values
casen2011["seg"]=casen2011["seg"].astype(str)

# We get the substring that identifies counties in the data base, and create a
# new column with it. Same with the region. Note that the Comuna_ID may be
# 4 or 5 strings long...
casen2011["Comuna_ID"]=casen2011["seg"].apply(lambda x: x[:4] if len(x)== 11 else x[:5])
casen2011["Region_ID"]=casen2011["seg"].apply(lambda x: x[:1] if len(x)== 11 else x[:2])

#Generating dummy variables for 3 different poverty cathegories:
casen2011["extreme_poverty_2011"] = casen2011["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2011["poverty_2011"] = casen2011["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2011["no_poverty_2011"] = casen2011["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)

# Grouping the data at a comuna level, we keep the mean values
casen2011_com = casen2011.groupby("Comuna_ID")[["extreme_poverty_2011", "poverty_2011", "no_poverty_2011",
"monetary_income_2011","total_income_2011"]].mean()




################################### CASEN 2013 #################################

#Converts the "seg" column from int to string values
casen2013["seg"]=casen2013["seg"].astype(str)

# We get the substring that identifies counties in the data base, and create a
# new column with it. Same with the region. Note that the Comuna_ID may be
# 4 or 5 strings long...
casen2013["Comuna_ID"]=casen2013["seg"].apply(lambda x: x[:4] if len(x)== 11 else x[:5])
casen2013["Region_ID"]=casen2013["seg"].apply(lambda x: x[:1] if len(x)== 11 else x[:2])

#Generating dummy variables for 3 different poverty cathegories:
casen2013["extreme_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2013["poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2013["no_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)

# Grouping the data at a comuna level, we keep the mean values
casen2013_com = casen2013.groupby("Comuna_ID")[["extreme_poverty_2013", "poverty_2013", "no_poverty_2013",
"monetary_income_2013","total_income_2013"]].mean()

###############################################################################

#In the following section we join the 4 Casen surveys

######################## The DATA MERGING ######################################

#Join 2006 data with 2009 data
merged1 =casen2006_com.join(casen2009_com)

#join 2006-2009 with 2011
merged2 = merged1.join(casen2011_com)

#join 2006-2009-2011 with 2013
Casen_ALL_com = merged2.join(casen2013_com)

# Drop counties that have missing values
# This could happen for severa reasons: county changed name/code/region, data quality issues, etc.
Casen_ALL_com.dropna(inplace = True)

# We still have 301/346 counties with information for the whole 2006-2009-2011-2013 series!!

###############################################################################

# In the following section, we add county names from COUNTY_CODES.csv
#to our merged data base

#################### PASTE COUNTY NAMES #######################################

#Read the file
cod_com = pd.read_csv("COUNTY_CODES.csv", usecols= ["region", "comuna", "zona", "comuna_name"],
sep=",", encoding='latin-1', index_col="comuna")

#Raname vars for consistency
cod_com.rename(columns={"comuna":"Comuna_ID", "zona":"Zone", "comuna_name":"county_name"}, inplace = True)

cod_com.index.rename("Comuna_ID", inplace = True)

#Set the index to int64 format
Casen_ALL_com.index=Casen_ALL_com.index.astype('int')

#Join the bases
Casen_ALL_com = Casen_ALL_com.join(cod_com)

#################### EXPORT THE MERGED DATA AS ONE .CSV FILE ###################

Casen_ALL_com.to_csv("Casen_all_final.csv")

# Note that, after this export, we did some edition through the command line
#(bash) in order to replace the latin characters (á, é, ,í ,ó, ú, ñ) with a
# their english closes relative (a,e,i,o,u,n). Djando join() command wasn't
# behaving well with the latin characters...

#The filed used in views.py is called Casen_all_final_edit.csv
