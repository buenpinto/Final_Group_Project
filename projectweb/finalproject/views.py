# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from django.shortcuts import render

# from django.urls import reverse # future versions.
from django.core.urlresolvers import reverse_lazy



###############################################################################
from os.path import join
from django.conf import settings
from django.urls import reverse
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def index(request):

    link = "http://electroners.com/online/wp-content/uploads/2016/05/COSTANERA_CENTER.jpg"

    return render(request, 'view_home.html', {'link':link})


def table2013(request):

    filename = join(settings.STATIC_ROOT, 'finalproject/Casen_all_final_edit.csv')

    casen_2013 = pd.read_csv(filename, usecols=["Comuna_ID","extreme_poverty_2013", "poverty_2013",
    "no_poverty_2013", "total_income_2013", "region", "county_name"])

    region = request.GET.get('region', '')

    if not region: region = request.POST.get('region', '13')

    region_casen_2013 = casen_2013.loc[casen_2013["region"]==int(region)]


    table = region_casen_2013.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
    table = table.replace('border="1"','border="0"')
    table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

    return render(request, 'view_table.html', {"title" :  REGION_DICT[region],

                                            "table" : table,

                                             'form_action' : reverse_lazy('finalproject:form') + "display_table/",
                                                       'form_method' : 'get',

                                                       'form' : InputForm({'region' : region}),
                                                       'region' : REGION_DICT[region],

                                                       })

###############################################################################

def cross_sectional2013(request, R=None, XVAR=None):

    filename = join(settings.STATIC_ROOT, 'finalproject/Casen_2013_vars.csv')
    casen_2013_extra_vars = pd.read_csv(filename)


    casen_2013_extra_vars = casen_2013_extra_vars.loc[casen_2013_extra_vars["Region_ID"]==int(R)]

    Reg = REGION_DICT[R]

    if ( XVAR == "1"):
        p=casen_2013_extra_vars.boxplot("total_income", by="education_level",figsize=(12,6))
        p.set_ylim([0, 2000000])

        plt.xlabel("Education Level")
        plt.ylabel("Household Income ($ CHP)")
        plt.title("Household Income vs Education Level (Chile, Year 2013, " + Reg + ")")
        plt.grid(True)

        from io import BytesIO
        figfile =BytesIO()

        plt.savefig(figfile, format='png')
        figfile.seek(0)

        return HttpResponse(figfile.read(), content_type="image/png")

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

        return HttpResponse("We are sorry! This county/query is not in our data base")

###############################################################################

def display_cross_sectional(request):

    region = request.GET.get('region','')
    if not region:region = request.POST.get('region','13')

    edu_pov = request.GET.get('edu_pov','')
    if not edu_pov : edu_pov = request.POST.get('edu_pov','1')

    return render(request, 'cross_sectional.html', {"title" : REGION_DICT[region],
                                                "plot" : reverse_lazy("finalproject:cross_sectional2013",
                                                kwargs={"R":region, "XVAR":edu_pov}),

                                             'form_action' : reverse_lazy('finalproject:form') + "display_cross_sectional/",
                                                 'form_method' : 'get',

                                                'form' : REG_VAR({'region' : region}),
                                                'region' : REGION_DICT[region],

                                                'edu_pov'  : VAR_DICT[edu_pov],

                                                               })


###############################################################################

def county(request, R=None, C=None, Cat=None):


   filename = join(settings.STATIC_ROOT, 'finalproject/Casen_all_final_edit.csv')

   casen_all = pd.read_csv(filename)

   casen_all["Comuna_ID"] = casen_all["Comuna_ID"].astype("str")

   county= casen_all.loc[casen_all["Comuna_ID"]== str(C)]["county_name"].values.tolist()[0]
   region = R
   cat = Cat


   if not region: region = request.POST.get('region', '13')

   nrows =len(casen_all.index)

   for i in range(0, nrows):
       s = casen_all.iloc[i]

       if(str(s[0]) == C):


           if (str(cat) == "1"):
               extreme_poverty = pd.DataFrame({"Year": [2006, 2009, 2011, 2013], "extreme_poverty":[s[1], s[6], s[11], s[16]]})
               p=extreme_poverty.plot(kind ="line", x="Year", y="extreme_poverty",
               xticks=[2005, 2006, 2009, 2011, 2013, 2014], marker='o', figsize=(12,6), color="blue")
               p.set_xticklabels(["", "2006", "2009", "2011", "2013", ""])
               plt.ylabel("Extreme Poverty (%)")
               plt.title("Extreme Poverty Evolution, Years 2006-2009-2011-2013 (Chile, " + county.title() + " county)"  , y=1.04)
               plt.grid(True)

               from io import BytesIO
               figfile =BytesIO()

               plt.savefig(figfile, format='png')
               figfile.seek(0)

               return HttpResponse(figfile.read(), content_type="image/png")

           elif (str(cat) == "2"):

               average_income = pd.DataFrame({"Year": [2006, 2009, 2011, 2013], "average_income":[s[5], s[10], s[15], s[20]]})
               p=average_income.plot(kind ="line", x="Year", y="average_income",
               xticks=[2005, 2006, 2009, 2011, 2013, 2014], marker='o', figsize=(12,6), color="red")
               p.set_xticklabels(["", "2006", "2009", "2011", "2013", ""])
               plt.ylabel("Average Income ($ CHP)")
               plt.title("Average Income Evolution, Years 2006-2009-2011-2013 (Chile, " + county.title() + " county)" , y=1.04)
               plt.grid(True)

               from io import BytesIO
               figfile =BytesIO()

               plt.savefig(figfile, format='png')
               figfile.seek(0)

               return HttpResponse(figfile.read(), content_type="image/png")

           else:

               return HttpResponse("We are sorry! This county/query is not in our data base")

################################ DISPLAYS #######################################

from .forms import InputForm, CAT, REG_VAR, C1, C2, C3, C4, C5, C6, C7, C8, C9, C10, C11, C12, C13
from .models import REGION_DICT, CAT_DICT, VAR_DICT, C1_DICT, C2_DICT, C3_DICT, C4_DICT, C5_DICT, C6_DICT, C7_DICT, C8_DICT, C9_DICT, C10_DICT, C11_DICT, C12_DICT, C13_DICT

def display_plot(request):

    cat= request.GET.get('cat', '')
    region= request.GET.get('region', '')


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

    if (cat == 2): cat= request.POST.get('cat','2')


    if not region:region = request.POST.get('region','13')


    if not cat: cat = request.POST.get('cat','1')

########################### region 1 ##########################################

    if (region == "1"):

        c1 = request.GET.get('c1','')
        if not c1: c1 = request.POST.get('c1','1101')

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


                                                       })

########################### region 2 ##########################################


    if (region == "2"):

        c2 = request.GET.get('c2','')
        if not c2: c2 = request.POST.get('c2','2101')

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


                                                       })


########################### region 3 ##########################################


    if (region == "3"):

        c3 = request.GET.get('c3','')
        if not c3: c3 = request.POST.get('c3','3101')

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


                                                       })


########################### region 4 ##########################################


    if (region == "4"):

        c4 = request.GET.get('c4','')
        if not c4: c4 = request.POST.get('c4','4101')

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


                                                       })


########################### region 5 ##########################################


    if (region == "5"):

        c5 = request.GET.get('c5','')
        if not c5: c5 = request.POST.get('c5','5101')

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


                                                       })


########################### region 6 ##########################################


    if (region == "6"):

        c6 = request.GET.get('c6','')
        if not c6: c6 = request.POST.get('c6','6101')

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


                                                       })


########################### region 7 ##########################################


    if (region == "7"):

        c7 = request.GET.get('c7','')
        if not c7: c7 = request.POST.get('c7','7101')

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


                                                       })


########################### region 8 ##########################################


    if (region == "8"):

        c8 = request.GET.get('c8','')
        if not c8: c8 = request.POST.get('c8','8101')

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


                                                       })



########################### region 9 ##########################################

    elif (region == "9"):

        c9 = request.GET.get('c9','')
        if not c9: c9 = request.POST.get('c9','9101')


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


                                                       })

########################### region 10 ##########################################

    elif (region == "10"):

        c10 = request.GET.get('c10','')
        if not c10: c10 = request.POST.get('c10','10101')


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


                                                       })

########################### region 11 ##########################################

    elif (region == "11"):

        c11 = request.GET.get('c11','')
        if not c11: c11 = request.POST.get('c11','11101')


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


                                                       })

########################### region 12 ##########################################

    elif (region == "12"):

        c12 = request.GET.get('c12','')
        if not c12: c12 = request.POST.get('c12','12101')


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


                                                       })

########################### region 13 ##########################################

    elif (region == "13"):

        c13 = request.GET.get('c13','')
        if not c13: c13 = request.POST.get('c13','13101')

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


                                                       })


################################ FORMS #########################################


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

###############################################################################


from django.views.generic import FormView

from django.views.generic import FormView

class FormClass(FormView):

    template_name = 'view_county.html'
    form_class = InputForm


#########################################################################
def get(self, request):
    region = request.GET.get('region', '13')

    return render(request, self.template_name, {'form_action' : reverse_lazy('finalproject:form'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'region' : region}),
                                                  'region' : REGION_DICT[region]})

def post(self, request):
    region = request.POST.get('region', '13')

    return render(request, self.template_name, {'form_action' : reverse_lazy('finalproject:form'),
                                                  'form_method' : 'get',
                                                  'form' : InputForm({'region' : region}),
                                                  'region' : REGION_DICT[region]})


def get_reader(request): # note: no other params.

  # state = request.GET.get('state', '')  # if we knew the parameters ...
  d = dict(request.GET._iterlists())
  return HttpResponse(str(d))
