
#Import somedjango  modules:
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.conf import settings
from django.urls import reverse

from os.path import join

#Other imports (pandas, etc.)
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


############################## INDEX ##########################################
#This fucntion just returns the link to the image used on the HOME
def index(request):

    link = "http://electroners.com/online/wp-content/uploads/2016/05/COSTANERA_CENTER.jpg"

    return render(request, 'view_home.html', {'link':link})

######################### FUNCTIONS ###########################################


######################### CROSS SECTIONAL PLOTS ################################

# This function generates "on the fly" the box plots shown on the Cross sectional section
# of the site. It takes a Region code (R) and a variable code (XVAR) as input parameters.
# The plots show the distribution of XVAR against Household Income, for each Region.
def cross_sectional2013(request, R=None, XVAR=None):

    #Import Casen_2013_vars.csv <- data file grouped at a Household level
    filename = join(settings.STATIC_ROOT, 'finalproject/Casen_2013_vars.csv')
    # Assign the data to a dataframe
    casen_2013_extra_vars = pd.read_csv(filename)

    # Keep only observations for the given region stored in R.
    casen_2013_extra_vars = casen_2013_extra_vars.loc[casen_2013_extra_vars["Region_ID"]==int(R)]

    # This assigns the name assiged to R in the Region dictionary into the var Reg
    Reg = REGION_DICT[R]

    # If the selected variable is "1" (i.e. Education)
    if ( XVAR == "1"):
        #generates the boxplot
        p=casen_2013_extra_vars.boxplot("total_income", by="education_level",figsize=(12,6))
        #limit the size of the y-axis for better visualizatin
        p.set_ylim([0, 2000000])

        #Label the x and y axis
        plt.xlabel("Education Level")
        plt.ylabel("Household Income ($ CHP)")
        #Give the plot a generic title (use Reg)
        plt.title("Household Income vs Education Level (Chile, Year 2013, " + Reg + ")")
        #Use a grid as background
        plt.grid(True)

        # Import BytesIO
        from io import BytesIO
        #Assing the plot to BytesIO
        figfile =BytesIO()
        #saves the file
        plt.savefig(figfile, format='png')
        #Initialized as 0
        figfile.seek(0)
        #returs a string with the "direction" of the image
        return HttpResponse(figfile.read(), content_type="image/png")

    # If the selected variable is "2" (i.e. Epmloyment)
    #The process is exactly the same as above!
    elif ( XVAR == "2"):

        p=casen_2013_extra_vars.boxplot("total_income", by="employed",figsize=(12,6))
        p.set_ylim([0, 2000000])

        plt.xlabel("Employed")
        plt.ylabel("Household Income($ CHP)")
        plt.title("Household Income vs. Employed (Chile, Year 2013, " + Reg + ")")
        plt.grid(True)

        from io import BytesIO
        figfile =BytesIO()

        plt.savefig(figfile, format='png')
        figfile.seek(0)

        return HttpResponse(figfile.read(), content_type="image/png")

    else:
        #If not found, returns a friendly response...
        return HttpResponse("We are sorry! This county/query is not in our data base")


########################## TIME SERIES PLOTS ####################################

def county(request, R=None, C=None, Cat=None):

  #Imports Casen_all_final_edit
   filename = join(settings.STATIC_ROOT, 'finalproject/Casen_all_final_edit.csv')

   #Assigns it to a dataframe
   casen_all = pd.read_csv(filename)

   #Changes the columns type to string
   casen_all["Comuna_ID"] = casen_all["Comuna_ID"].astype("str")

   # We get the county name (this is because we have 13 different county dictionaries)
   county= casen_all.loc[casen_all["Comuna_ID"]== str(C)]["county_name"].values.tolist()[0]

   # We have to search for the given county along the whole dataframe
   nrows =len(casen_all.index)

   #Start of the loop:
   for i in range(0, nrows):
       #s stores the all the column values in each row. s[0]=index=county id
       s = casen_all.iloc[i]
       # if s[0]= C (= input for the county id from the form!)
       if(str(s[0]) == C):

           #Then if Cat ==1 (=> Poverty category selected)
           if (str(Cat) == "1"):
               #Generate a data frame with poverty values for years 2006-2009-2011-2013
               extreme_poverty = pd.DataFrame({"Year": [2006, 2009, 2011, 2013], "extreme_poverty":[s[1], s[6], s[11], s[16]]})
               #plot this data fame as a line.
               p=extreme_poverty.plot(kind ="line", x="Year", y="extreme_poverty",
               xticks=[2005, 2006, 2009, 2011, 2013, 2014], marker='o', figsize=(12,6), color="blue")
               #Label the x-axis. Leave some space on the borders.
               p.set_xticklabels(["", "2006", "2009", "2011", "2013", ""])
               #Label the y-axis
               plt.ylabel("Extreme Poverty (%)")
               #Appropriate generic title for each county
               plt.title("Extreme Poverty Evolution, Years 2006-2009-2011-2013 (Chile, " + county.title() + " county)"  , y=1.04)
               #include a gris in the background
               plt.grid(True)

               #Again, same as in cross_sectional, store the plot as bytes using BytesIO!
               from io import BytesIO
               figfile =BytesIO()

               plt.savefig(figfile, format='png', bbox_inches='tight')
               figfile.seek(0)

               return HttpResponse(figfile.read(), content_type="image/png")

            #Same as above, but now making a time series plot for Income for the given period
           elif (str(Cat) == "2"):

               average_income = pd.DataFrame({"Year": [2006, 2009, 2011, 2013], "average_income":[s[5], s[10], s[15], s[20]]})
               p=average_income.plot(kind ="line", x="Year", y="average_income",
               xticks=[2005, 2006, 2009, 2011, 2013, 2014], marker='o', figsize=(12,6), color="red")
               p.set_xticklabels(["", "2006", "2009", "2011", "2013", ""])
               plt.ylabel("Average Income ($ CHP)")
               plt.title("Average Income Evolution, Years 2006-2009-2011-2013 (Chile, " + county.title() + " county)" , y=1.04)
               plt.grid(True)

               from io import BytesIO
               figfile =BytesIO()

               plt.savefig(figfile, format='png', bbox_inches='tight')
               figfile.seek(0)

               return HttpResponse(figfile.read(), content_type="image/png")

           else:

               return HttpResponse("We are sorry! This county/query is not in our data base")


###############################################################################

################################ DISPLAYS #######################################
# Import the forms and dictionaries generates in forms.py and models.py

from .forms import InputForm, CAT, REG_VAR, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13
from .models import REGION_DICT, CAT_DICT, VAR_DICT, C1_DICT, C2_DICT, C3_DICT, C4_DICT, C5_DICT, C6_DICT, C7_DICT, C8_DICT, C9_DICT, C10_DICT, C11_DICT, C12_DICT, C13_DICT


#####################  TABLE (Generated and rendered) ##########################

# The following function generates and renders the tables
#displayed into the view_table.html' template, using the URL
# http://127.0.0.1:8000/finalproject/display_table/

def table2013(request):
    # Import the Casen_all_final_edit.csv file generated by merge_all.py
    filename = join(settings.STATIC_ROOT, 'finalproject/Casen_all_final_edit.csv')

    # Assign the data to a dataframe, keep these columns only
    casen_2013 = pd.read_csv(filename, usecols=["region", "Comuna_ID","county_name", "extreme_poverty_2013", "poverty_2013",
     "total_income_2013" ])

    # Some renaming for a more friendly display
    casen_2013.rename(columns={"region":"Region", "extreme_poverty_2013":"% Extremely Poor",
    "poverty_2013":"% Poor","total_income_2013":"Average Household Income ($ CHP)",
    "county_name":"County Name"}, inplace=True)

    # Check if the drop down list has been requested
    region = request.GET.get('region', '')
    #If not, assign a value (region == 13)
    if not region: region = request.POST.get('region', '13')

    # Keep only the portion of the table corresponding to "region"
    region_casen_2013 = casen_2013.loc[casen_2013["Region"]==int(region)]

    #Generate the table, define styles, etc.
    table = region_casen_2013.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    #return the render to 'view_table.html' with the given parameters:
    return render(request, 'view_table.html', {"title" :  REGION_DICT[region],

                                            "table" : table,

                                             'form_action' : reverse_lazy('finalproject:form') + "display_table/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       })

######################## DISPLAY FOR CROSS SECTIONAL PLOTS ####################

# The following function renders the plots generated by the cross_sectional2013
# function into the 'cross_sectional.html' template, using the URL
# http://127.0.0.1:8000/finalproject/display_cross_sectional/

def display_cross_sectional(request):

    #check the region form input
    region = request.GET.get('region','')
    # if null, assign a default value
    if not region:region = request.POST.get('region','13')
    #check the variable (education/poverty) form input
    edu_pov = request.GET.get('edu_pov','')
    # if null, assign a default value
    if not edu_pov : edu_pov = request.POST.get('edu_pov','1')

    # render the parameters to 'cross_sectional.html', using reverse_lazy and
    # on the cross_sectional2013 function
    return render(request, 'cross_sectional.html', {"title" : REGION_DICT[region],
                                                "plot" : reverse_lazy("finalproject:cross_sectional2013",
                                                kwargs={"R":region, "XVAR":edu_pov}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_cross_sectional/",
                                                 'form_method' : 'get',

                                                'form' : REG_VAR({'region' : region}),
                                                'region' : REGION_DICT[region],

                                                'edu_pov'  : VAR_DICT[edu_pov],

                                                               })

###################### DISPLAYS FOR THE MAPS SECTION ###########################
#The following function renders a link for the image that contains a cloropleth map for the selected region,
# passing it to the template 'view_map.html' using the URL http://127.0.0.1:8000/finalproject/display_map/

# Note: All map images are stored as static files in "~static/finalproject/"

def display_map(request):

    # check the region form
    region= request.GET.get('region', '')
    # if null, assign default value
    if not region:region = request.POST.get('region','13')

    # the link variable stores the direction of each map, stored in "~static/finalproject/"
    # Note that these maps where generated ex-ante through gis.py and gis_region.py
    link = "/finalproject/map_" + str(region) +".png"

    #renders the given parameter
    return render(request, 'view_map.html', {"title":REGION_DICT[region],
                                                "link":link,

                                             'form_action' : reverse_lazy('finalproject:form') + "display_map/",
                                             'form_method' : 'get',

                                            'form' : InputForm({'region' : region}),
                                            'region' : REGION_DICT[region],

                                                       })



################### DISPLAYS THE TIME SERIES PLOTS #############################

# The following function renders the plots generated by the county() function
# into the 'view_county.html' template, using the URL
# http://127.0.0.1:8000/finalproject/display_plot/


def display_plot(request):

    # check the cat (poverty/income) and region form
    cat= request.GET.get('cat', '')
    region= request.GET.get('region', '')

    # check all the county forms
    # Note that we had to create 13 forms and 13 dictionaries in order to be able to
    # display a county list as a fucntion of a regional selection. There are 301 counties
    # in the 13 dictionaries, one county dictionary per region. For example, all counties
    # located in region one are displayed in the c1 form, listed in the C1_DICT dictionary. And so on...

    c1 = request.GET.get('c1','')
    c2 = request.GET.get('c2','')
    c3 = request.GET.get('c3','')
    c4 = request.GET.get('c4','')
    c5 = request.GET.get('c5','')
    c6 = request.GET.get('c6','')
    c7 = request.GET.get('c7','')
    c8 = request.GET.get('c8','')
    c9 = request.GET.get('c9','')
    c10 = request.GET.get('c10','')
    c11 = request.GET.get('c11','')
    c12 = request.GET.get('c12','')
    c13 = request.GET.get('c13','')

    #Checking for previous selection (i.e. updating "region" with "county" sel)
    for i in range (1,13):
        if (request.GET.get('c'+str(i),'')): region = str(i)

    # keep the selected category
    if (cat == 2): cat= request.POST.get('cat','2')

    # Default region if null
    if not region:region = request.POST.get('region','13')

    # Default cat if null
    if not cat: cat = request.POST.get('cat','1')

# In the following lines, we produced a somehow ineficient code, checking separately
# for each region. Though it is clear that this could be done more efficiently, we weren't
# sure on how to call region level indexed functions (e.g. C1_DICT[c1] or C1({'c1': c1}),)
# as a function of an iterative parameter (e.g. the "i" value on a for loop).

########################### region 1 ##########################################

    # check if the selected region is region 1
    if (region == "1"):

        #Then, we check the county level parameter from the form
        c1 = request.GET.get('c1','')
        # If null, we assign the regional default (i.e. county == 1101)
        if not c1: c1 = request.POST.get('c1','1101')

        # generate a link for a map stored in static, showing the selected county

        link = "/finalproject/map_" + str(c1) +".png"
        # renders the given parameters, using reverse_laze on the county() function.
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C1_DICT[c1],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c1, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C1({'c1': c1}),
                                                       'county'  : C1_DICT[c1],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,
                                                       'c1':c1,

                                                       })

###############################################################################

# All the following code, across the 12 remaining regions, is the same
########################### region 2 ##########################################

    if (region == "2"):

        c2 = request.GET.get('c2','')
        if not c2: c2 = request.POST.get('c2','2101')
        link = "/finalproject/map_" + str(c2) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C2_DICT[c2],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c2, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C2({'c2': c2}),
                                                       'county'  : C2_DICT[c2],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                        'link' : link,

                                                       })


########################### region 3 ##########################################

    if (region == "3"):

        c3 = request.GET.get('c3','')
        if not c3: c3 = request.POST.get('c3','3101')

        link = "/finalproject/map_" + str(c3) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C3_DICT[c3],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c3, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C3({'c3': c3}),
                                                       'county'  : C3_DICT[c3],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                        'link' : link,

                                                       })


########################### region 4 ##########################################

    if (region == "4"):

        c4 = request.GET.get('c4','')
        if not c4: c4 = request.POST.get('c4','4101')

        link = "/finalproject/map_" + str(c4) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C4_DICT[c4],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c4, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C4({'c4': c4}),
                                                       'county'  : C4_DICT[c4],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                        'link' : link,

                                                       })


########################### region 5 ##########################################

    if (region == "5"):

        c5 = request.GET.get('c5','')
        if not c5: c5 = request.POST.get('c5','5101')

        link = "/finalproject/map_" + str(c5) +".png"
        return render(request, 'view_county.html', {"title" : REGION_DICT[region] +", County: " + C5_DICT[c5],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c5, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C5({'c5': c5}),
                                                       'county'  : C5_DICT[c5],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })


########################### region 6 ##########################################

    if (region == "6"):

        c6 = request.GET.get('c6','')
        if not c6: c6 = request.POST.get('c6','6101')

        link = "/finalproject/map_" + str(c6) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C6_DICT[c6],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c6, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C6({'c6': c6}),
                                                       'county'  : C6_DICT[c6],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })


########################### region 7 ##########################################

    if (region == "7"):

        c7 = request.GET.get('c7','')
        if not c7: c7 = request.POST.get('c7','7101')

        link = "/finalproject/map_" + str(c7) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C7_DICT[c7],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c7, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C7({'c7': c7}),
                                                       'county'  : C7_DICT[c7],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })


########################### region 8 ##########################################

    if (region == "8"):

        c8 = request.GET.get('c8','')
        if not c8: c8 = request.POST.get('c8','8101')

        link = "/finalproject/map_" + str(c8) +".png"
        return render(request, 'view_county.html', {"title" :   REGION_DICT[region] +", County: " + C8_DICT[c8],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c8, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C8({'c8': c8}),
                                                       'county'  : C8_DICT[c8],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })



########################### region 9 ##########################################

    elif (region == "9"):

        c9 = request.GET.get('c9','')
        if not c9: c9 = request.POST.get('c9','9101')

        link = "/finalproject/map_" + str(c9) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C9_DICT[c9],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c9, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C9({'c9': c9}),
                                                       'county'  : C9_DICT[c9],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })

########################### region 10 ##########################################

    elif (region == "10"):

        c10 = request.GET.get('c10','')
        if not c10: c10 = request.POST.get('c10','10101')

        link = "/finalproject/map_" + str(c10) +".png"
        return render(request, 'view_county.html', {"title" :   REGION_DICT[region] +", County: " + C10_DICT[c10],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c10, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C10({'c10': c10}),
                                                       'county'  : C10_DICT[c10],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })

########################### region 11 ##########################################

    elif (region == "11"):

        c11 = request.GET.get('c11','')
        if not c11: c11 = request.POST.get('c11','11101')

        link = "/finalproject/map_" + str(c11) +".png"
        return render(request, 'view_county.html', {"title" :   REGION_DICT[region] +", County: " + C11_DICT[c11],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c11, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C11({'c11': c11}),
                                                       'county'  : C11_DICT[c11],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })

########################### region 12 ##########################################

    elif (region == "12"):

        c12 = request.GET.get('c12','')
        if not c12: c12 = request.POST.get('c12','12101')

        link = "/finalproject/map_" + str(c12) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C12_DICT[c12],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c12, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C12({'c12': c12}),
                                                       'county'  : C12_DICT[c12],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })

########################### region 13 ##########################################

    elif (region == "13"):

        c13 = request.GET.get('c13','')
        if not c13: c13 = request.POST.get('c13','13101')

        link = "/finalproject/map_" + str(c13) +".png"
        return render(request, 'view_county.html', {"title" :  REGION_DICT[region] +", County: " + C13_DICT[c13],
                                             "pic_county" : reverse_lazy("finalproject:county", kwargs={"R":region, "C":c13, "Cat":cat}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_plot/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       'form2': C13({'c13': c13}),
                                                       'county'  : C13_DICT[c13],

                                                       #'form_cat': Cat({'cat' : cat}),
                                                       'cat'  : CAT_DICT[cat],
                                                       'link' : link,


                                                       })


################################ FORM #########################################
# We use this function with reverse_lazy on the functions above, to get the root URL.
def form(request):

    region = request.GET.get('region', '')
    #c13 = request.GET.get('c13', '')

    if not region : region = request.POST.get('region', '13')
    #if not c13 : c13= request.POST.get('c13', '13101')

    params = {'form_action' : reverse_lazy('finalproject:form'),
              'form_method' : 'get',
              'form' : InputForm({'region' : region}),
              'region' : REGION_DICT[region],

              }

    return render(request, 'view_county.html', params)
