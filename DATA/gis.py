#need to type p34a on bash before importing geopandas

import geopandas as gpd
import pandas as pd
import numpy  as np
from matplotlib import pyplot as plt
import os

casen2013 = pd.read_csv("Casen_2013_vars.csv")


casen2013 = casen2013.groupby("Comuna_ID")[["Region_ID", "education_level", "employed","total_income"]].mean()


chile_df = gpd.read_file("data/cl_comunas_geo.shp")


chile_df.rename(columns={'ID_2002':'Comuna_ID'}, inplace = True)

chile_df["Comuna_ID"]=chile_df["Comuna_ID"].astype(int)

chile_df.set_index(chile_df["Comuna_ID"], inplace = True)



chile_merged = chile_df.join(casen2013, how = "outer")

chile_merged=chile_merged[chile_merged["NOMBRE"].notnull()]


nrows=len(chile_merged.index)
#print(nrows)

#Changes the working directory
os.chdir("C:\cygwin64\home\Cristobal\Final_Group_Project\DATA\Maps")

#The loop that generates the plots:
for i in range(1, nrows):
    com = chile_merged.index.tolist()[i]
    s = chile_merged.iloc[i]
    chile_merged["selection"] =chile_merged["Comuna_ID"].apply(lambda x: 1 if x==com  else 0)


    figure = chile_merged.plot(column="selection", cmap='OrRd', categorical=True, figsize=(3,6))

    figure.set_axis_off()
    name ="map_" + str(com) + ".png"
    #plt.show()
    figure.get_figure().savefig(name)
