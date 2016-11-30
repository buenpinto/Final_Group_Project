#need to type p34a on bash before importing geopandas

import geopandas as gpd
import pandas as pd
import numpy  as np
from matplotlib import pyplot as plt
import os

casen2013 = pd.read_csv("Casen_2013_vars.csv")

#print(casen2013.dtypes)

casen2013 = casen2013.groupby("Comuna_ID")[["Region_ID", "education_level", "employed","total_income"]].mean()

#chile_df = gpd.read_file("data/division_comunal.shp")
chile_df = gpd.read_file("GIS_Data/cl_comunas_geo.shp")


chile_df.rename(columns={'ID_2002':'Comuna_ID'}, inplace = True)

chile_df["Comuna_ID"]=chile_df["Comuna_ID"].astype(int)

chile_df.set_index(chile_df["Comuna_ID"], inplace = True)



chile_merged = chile_df.join(casen2013, how = "outer")

chile_merged=chile_merged[chile_merged["NOMBRE"].notnull()]


chile_merged["Comuna_ID"] = chile_merged["Comuna_ID"].astype(str)
chile_merged["Region_ID"]=chile_merged["Comuna_ID"].apply(lambda x: x[:1] if len(x)== 6 else x[:2])


chile_merged=chile_merged[chile_merged["total_income"].notnull()]



nrows=len(chile_merged.index)

#Changes the working directory
os.chdir("C:\cygwin64\home\Cristobal\Final_Group_Project\DATA\Maps")

################################################################################

#The loop that generates the plots:
for i in range(1, 2):
    com = chile_merged.index.tolist()[i]
    s = chile_merged.iloc[i]
    chile_merged["selection"] =chile_merged["Region_ID"].apply(lambda x: 1 if x==str(i)  else 0)

    chile_merged["centroid"]=chile_merged[chile_merged["selection"]==1].geometry.centroid
    figure = chile_merged[chile_merged["selection"]==1].plot(column="total_income",
    scheme='QUANTILES', k=5, cmap='Blues', alpha=1, figsize=(15,15), legend=True)

    plt.legend(loc='upper right')
    figure.set_axis_off()
    plt.title("Income distribution by quintiles, Region "+str(i).upper()+ " , Chile, year 2013",
    y=1.08, fontsize=25)
    name ="map_" + str(i) + ".png"

    #plt.show()
    figure.get_figure().savefig(name)
