from django.conf.urls import url

from . import views

app_name = 'finalproject'
urlpatterns = [

###############################################################################
    #Index (Site URL)
    url(r'Home/$', views.index, name ='home'),

############################# TABLE SECTION #####################################
    #ROOT
    url(r'^$', views.table2013, name ='table2013'),
    #Site URL
    url(r'display_table/$', views.table2013, name='display_table'),

############################# MAPS SECTION ######################################
    #ROOT
    url(r'^$', views.display_map, name ='display_map'),
    #Site URL
    url(r'display_map/$', views.display_map, name='display_map'),

############################# CROSS SECTIONAL PLOTS SECTION ####################
    #ROOT
    url(r'(?P<R>[0-9]+)/(?P<XVAR>[0-9]+)/CS$', views.cross_sectional2013, name='cross_sectional2013'),
    #Site URL
    url(r'display_cross_sectional/$', views.display_cross_sectional, name='display_cross_sectional'),


############################# TIME SERIES PLOTS SECTION ########################

    #ROOT
    url(r'^$', views.county, name ='county'),
    #PARAMETERS
    url(r'(?P<R>[0-9]+)/(?P<C>[0-9]+)/(?P<Cat>[0-9]+)/$', views.county, name ='county'),
    #Site URL
    url(r'display_plot/$', views.display_plot, name='display_plot'),

#################################### OTHERS ##################################
    #Form
    url(r'^$', views.form, name ='form'),
##############################################################################

]
