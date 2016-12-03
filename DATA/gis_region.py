#need to type p34a on bash before importing geopandas
# Imorting the modules we'll be using

import geopandas as gpd
import pandas as pd
from matplotlib import pyplot as plt
import os


# This python script generates 13 maps, one for each of Chile's 13 regions. Each map
# is of the cloropleth type, showing the income distribution within that region (quintiles).
# The images are named as map_region_code.png, in order to be able to request them
# "on demand" at a later stage (i.e. from views.py)

############################## IMPORT/GROUP CASEN SURVEY #########################################
# We work with casen 2013, since it has the more up to date  data
# This is the (already cleaned) output from edit_Casen2013.py
casen2013 = pd.read_csv("Casen_2013_vars.csv")

# Group the data at a county level, we keep the mean values
casen2013 = casen2013.groupby("Comuna_ID")[["Region_ID", "education_level", "employed","total_income"]].mean()

##########################IMPORT CHILE COUNTIES SHAPEFILE ##################################

#Import the shapefile
chile_df = gpd.read_file("GIS_Data/cl_comunas_geo.shp")

# Rename the index variables to be able to do the join()
chile_df.rename(columns={'ID_2002':'Comuna_ID'}, inplace = True)

# Index must be of the same type before the join()
chile_df["Comuna_ID"]=chile_df["Comuna_ID"].astype(int)

# Set county id as index on the shapefile as well
chile_df.set_index(chile_df["Comuna_ID"], inplace = True)

############################### DATA MERGING ##############################################

# Join the shapefile with the casen2013 data

chile_merged = chile_df.join(casen2013, how = "outer")

# Keep all the original rows in the shapefile (since we want to show a full map of Chile)
# but drop unmatched rows from casen2013 variables.
chile_merged=chile_merged[chile_merged["NOMBRE"].notnull()]


######################## SOME FINAL EDITION ################################################
# Change county id to string to extract the region id:

chile_merged["Comuna_ID"] = chile_merged["Comuna_ID"].astype(str)

# Extract the region id from the county id (first 1 (or 2) strings)
chile_merged["Region_ID"]=chile_merged["Comuna_ID"].apply(lambda x: x[:1] if len(x)== 6 else x[:2])

# Keep only those counties that have non-null income values
chile_merged=chile_merged[chile_merged["total_income"].notnull()]



############################# THE LOOP ####################################################



#Changes the working directory
os.chdir("C:\cygwin64\home\Cristobal\Final_Group_Project\DATA\Maps")

#################################THE LOOP #################################################

#The generate one map (image) per each of the 13 regions
for i in range(1, 14):

    #We create a dummy variable for the "i" region
    chile_merged["selection"] =chile_merged["Region_ID"].apply(lambda x: 1 if x==str(i)  else 0)

    # We create a cloropleth map for that particular region only. We use quintiles (i.e. quatiles
    # with k=5).
    figure = chile_merged[chile_merged["selection"]==1].plot(column="total_income",
    scheme='QUANTILES', k=5, cmap='Blues', alpha=1, figsize=(15,15), legend=True)

    # Positionig of the legend
    plt.legend(loc='upper right')
    # Get rid of the axis
    figure.set_axis_off()
    # Plot title
    plt.title("Income distribution by quintiles, Region "+str(i).upper()+ " , Chile, year 2013",
    y=1.08, fontsize=25)
    # save the image as map_region_code.png
    name ="map_" + str(i) + ".png"

    #save the image to the given directory
    figure.get_figure().savefig(name)
