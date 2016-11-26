import pandas as pd

casen2013 = pd.read_csv("CASEN_2013.csv", usecols=["folio", "o",
"pobreza_mn", "ymonecorh", "ypchtot", "e6a","o1"], encoding='latin-1')



casen2013.rename(columns={'folio':'seg', "ymonecorh":"monetary_income_2013",
"ypchtot":"total_income_2013", "e6a":"education_level","o1":"employed"} , inplace = True)




casen2013 = casen2013.sort_values(by = "seg")

casen2013["seg"]=casen2013["seg"].astype(str)

casen2013["Comuna_ID"]=casen2013["seg"].apply(lambda x: x[:4] if len(x)== 11 else x[:5])
casen2013["Region_ID"]=casen2013["seg"].apply(lambda x: x[:1] if len(x)== 11 else x[:2])

#Generating the some dummy variables with the data:

casen2013["extreme_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres extremos"  else 0)
casen2013["poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="pobres no extremos"  else 0)
casen2013["no_poverty_2013"] = casen2013["pobreza_mn"].apply(lambda x: 1 if x=="no pobres"  else 0)

########################### Education vars ####################################

#If Non response, then we don't consider them (i.e. ed=0)
casen2013["education_level_0"] = casen2013["education_level"].apply(lambda x: 0 if x=="ns/nr"  else 0)

casen2013["education_level_1"] = casen2013["education_level"].apply(lambda x: 1 if x=="nunca asistió"  else 0)
casen2013["education_level_2"] = casen2013["education_level"].apply(lambda x: 2 if x=="jardín infantil/sala cuna"  else 0)
casen2013["education_level_3"] = casen2013["education_level"].apply(lambda x: 3 if x=="kinder/pre-kinder"  else 0)
casen2013["education_level_4"] = casen2013["education_level"].apply(lambda x: 4 if x=="educación especial (diferencial)"  else 0)
casen2013["education_level_5"] = casen2013["education_level"].apply(lambda x: 5 if x=="primaria/preparatoria (sistema antiguo)"  else 0)
casen2013["education_level_6"] = casen2013["education_level"].apply(lambda x: 6 if x=="educación básica"  else 0)
casen2013["education_level_7"] = casen2013["education_level"].apply(lambda x: 7 if x=="humanidades (sistema antiguo)"  else 0)
casen2013["education_level_8"] = casen2013["education_level"].apply(lambda x: 8 if x=="educación media científico-humanista"  else 0)
casen2013["education_level_9"] = casen2013["education_level"].apply(lambda x: 9 if x=="técnica, comercial, industrial o normalista (sistema antiguo) "  else 0)
casen2013["education_level_10"] = casen2013["education_level"].apply(lambda x: 10 if x=="educación media técnica profesional"  else 0)
casen2013["education_level_11"] = casen2013["education_level"].apply(lambda x: 11 if x=="técnico nivel superior (carreras de 1 a 3 años)"  else 0)
casen2013["education_level_12"] = casen2013["education_level"].apply(lambda x: 12 if x=="profesional (carreras de 4 o más años) "  else 0)
casen2013["education_level_13"] = casen2013["education_level"].apply(lambda x: 13 if x=="postgrado"  else 0)

casen2013["education_level_tot"]= casen2013["education_level_0"]
for i in range (1,14):
    casen2013["education_level_tot"]=casen2013["education_level_tot"]+casen2013["education_level_{}".format(i)]



#Employment
casen2013["employed"]=casen2013["employed"].apply(lambda x: 1 if x=="sí"  else 0)



#Final edition

casen2013=casen2013[["Comuna_ID","Region_ID", "extreme_poverty_2013",
"poverty_2013","no_poverty_2013","education_level_tot","employed","total_income_2013"]]

casen2013.rename(columns={"education_level_tot":"education_level", "total_income_2013":"total_income"} , inplace = True)



#print(casen2013)

casen2013.to_csv("Casen_2013_final.csv")

casen2013 = casen2013[["Comuna_ID","Region_ID", "education_level","employed", "total_income"]]

casen2013.to_csv("Casen_2013_vars.csv")
