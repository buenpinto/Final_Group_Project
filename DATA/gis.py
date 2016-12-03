#need to type p34a on bash before importing geopandas
# Imorting the modules we'll be using

import geopandas as gpd
import pandas as pd
from matplotlib import pyplot as plt
import os

# This python script generates 333 images of Chile, each one of them showing
# a different county being "selected". The images are named as map_county_code.png,
# in order to be able to request them "on demand" at a later stage (i.e. from views.py)

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

############################# THE LOOP ####################################################

# We´ll loop across all rows (one image generated per row=county)
nrows=len(chile_merged.index)

#Changes the working directory for exporting the images
os.chdir("C:\cygwin64\home\Cristobal\Final_Group_Project\DATA\Maps")

#This is loop that generates the map images:

for i in range(1, nrows):
    com = chile_merged.index.tolist()[i] # index is the county id
    s = chile_merged.iloc[i] # this creates a list with all the row values
    # We create a county level dummy
    chile_merged["selection"] =chile_merged["Comuna_ID"].apply(lambda x: 1 if x==com  else 0)

    #We generate a cloropleth map with this dummy as input => only that county will be highlighted in the map!
    figure = chile_merged.plot(column="selection", cmap='OrRd', categorical=True, figsize=(3,6))
    #get rid of the axis
    figure.set_axis_off()
    # create a string for the map name that identifies the county.
    name ="map_" + str(com) + ".png"
    #save the image to the given directory
    figure.get_figure().savefig(name)
