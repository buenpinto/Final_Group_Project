This folder contains the raw data used to generate the
data bases used on the project. That is, 4 cross sectional 
Casen surveys with selected variables plus a data base 
(i.e. COUNTY_CODES.csv) that contains the name of each county 
with its county ID (the identifyier used in the surveys)
This are, for each year: 

-Casen_2006.csv
-Casen_2009.csv
-Casen_2011.csv
-Casen_2013.csv

-COUNTY_CODES.csv


The folder also contains some python scripts, that were used to:

(i)  - merge_all.py --> merge and clean all the Casen surveys (2006 to 2013)
(ii) - editCasen2013.py --> import some extra variables from the Casen_2013.csv 
                            file to use on our "Cross sectional" section. (see 
			    "dislay_cross_sectional" and "cross_sectional2013" 
			    views on views.py)

Finally, we also have the output data from the previuos scripts:

- Casen_all_final.csv --> merged data base; output from merge_all.py
- Casen_all_final_edit.csv --> same as Casen_all_final.csv, bue without some characters 
			      (á,é,í,ó, ú, ñ) that were causing import problems with the 
			       "join(settings.STATIC_ROOT,.." instruction in django
- Casen_2013_vars.csv --> cleaned Casen2013 data base with additional education and 
			  employment level variables(used on our "Cross sectional" section). 
