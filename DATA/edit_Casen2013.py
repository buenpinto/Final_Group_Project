#Importing pandas
import pandas as pd

# This python script imports a more rich data base for casen year 2013 only.
#We then generate the education cathegories and employment indicator (binary)
# that we'll use in our cross sectional plots.

########################## IMPORT & CLEAN  ####################################

#Import data from the casen 2013 survey
#this time keep some extra variables for education and employment status
casen2013 = pd.read_csv("CASEN_2013.csv", usecols=["folio", "o",
"pobreza_mn", "ymonecorh", "ypchtot", "e6a","o1"], encoding='latin-1')

# Some variable renaming (some names are not obvious)
# We used a codebook for understanding the Casen variable labeling...
casen2013.rename(columns={'folio':'seg', "ymonecorh":"monetary_income_2013",
"ypchtot":"total_income_2013", "e6a":"education_level","o1":"employed"} , inplace = True)

#Converts the "seg" column from int to string values
casen2013["seg"]=casen2013["seg"].astype(str)

# We get the substring that identifies counties in the data base, and create a
# new column with it. Same with the region. Note that the Comuna_ID may be
# 4 or 5 strings long...
casen2013["Comuna_ID"]=casen2013["seg"].apply(lambda x: x[:4] if len(x)== 11 else x[:5])
casen2013["Region_ID"]=casen2013["seg"].apply(lambda x: x[:1] if len(x)== 11 else x[:2])


############# Povery dummies (same as in merge_all.py) ######################

#Generating dummy variables for 3 different poverty cathegories:
casen2013["extreme_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2013["poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2013["no_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)


########################### Education cathegories ##############################

#If non-response, then we give them a value of "0"
casen2013["education_level_0"] = casen2013["education_level"].apply(lambda x: 0 if x=="ns/nr"  else 0)

# Higher number means higher education level
casen2013["education_level_1"] = casen2013["education_level"].apply(lambda x: 1 if x=="nunca asistió"  else 0)
casen2013["education_level_2"] = casen2013["education_level"].apply(lambda x: 2 if x=="jardín infantil/sala cuna"  else 0)
casen2013["education_level_3"] = casen2013["education_level"].apply(lambda x: 3 if x=="kinder/pre-kinder"  else 0)
casen2013["education_level_4"] = casen2013["education_level"].apply(lambda x: 4 if x=="educación especial (diferencial)"  else 0)
casen2013["education_level_5"] = casen2013["education_level"].apply(lambda x: 5 if x=="primaria/preparatoria (sistema antiguo)"  else 0)
casen2013["education_level_6"] = casen2013["education_level"].apply(lambda x: 6 if x=="educación básica"  else 0)
casen2013["education_level_7"] = casen2013["education_level"].apply(lambda x: 7 if x=="humanidades (sistema antiguo)"  else 0)
casen2013["education_level_8"] = casen2013["education_level"].apply(lambda x: 8 if x=="educación media científico-humanista"  else 0)
casen2013["education_level_9"] = casen2013["education_level"].apply(lambda x: 9 if x=="técnica, comercial, industrial o normalista (sistema antiguo)"  else 0)
casen2013["education_level_10"] = casen2013["education_level"].apply(lambda x: 10 if x=="educación media técnica profesional"  else 0)
casen2013["education_level_11"] = casen2013["education_level"].apply(lambda x: 11 if x=="técnico nivel superior (carreras de 1 a 3 años)"  else 0)
casen2013["education_level_12"] = casen2013["education_level"].apply(lambda x: 12 if x=="profesional (carreras de 4 o más años)"  else 0)
casen2013["education_level_13"] = casen2013["education_level"].apply(lambda x: 13 if x=="postgrado"  else 0)

# This instruction collapses all the above into one, cathegorical variable called education_level_tot
casen2013["education_level_tot"]= casen2013["education_level_0"]
for i in range (1,14):
    casen2013["education_level_tot"]=casen2013["education_level_tot"]+casen2013["education_level_{}".format(i)]

########################### Employment dummy ##############################

#1 means employed, 0 means unemployed
casen2013["employed"]=casen2013["employed"].apply(lambda x: 1 if x=="sí"  else 0)


############################### Final Edition #################################

# Keep this subset of variables only
casen2013=casen2013[["Comuna_ID","Region_ID", "extreme_poverty_2013",
"poverty_2013","no_poverty_2013","education_level_tot","employed","total_income_2013"]]

#Some renaming
casen2013.rename(columns={"education_level_tot":"education_level", "total_income_2013":"total_income"} , inplace = True)


############################ EXPORT THE DATA ###################################

# Keep yet another subset:
casen2013 = casen2013[["Comuna_ID","Region_ID", "education_level","employed", "total_income"]]

#Export into Casen_2013_vars.csv
# Note that we didn't group at a county level this time => we want to show
# household level variation in the cross-sectional analysis.
casen2013.to_csv("Casen_2013_vars.csv")
