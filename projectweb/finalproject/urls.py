from django.conf.urls import url

from . import views

app_name = 'finalproject'
urlpatterns = [

###############################################################################
    #Index
    url(r'Home/$', views.index, name ='home'),

    #Table section
    url(r'^$', views.table2013, name ='table2013'),

    url(r'display_table/$', views.table2013, name='display_table'),


    url(r'^$', views.display_map, name ='display_map'),

    url(r'display_map/$', views.display_map, name='display_map'),


    #Cross sectional plots section
    #url(r'^$', views.cross_sectional2013, name='cross_sectional2013'),
    url(r'(?P<R>[0-9]+)/(?P<XVAR>[0-9]+)/CS$', views.cross_sectional2013, name='cross_sectional2013'),

    #url(r'^$', views.display_cross_sectional, name='display_cross_sectional'),

    url(r'display_cross_sectional/$', views.display_cross_sectional, name='display_cross_sectional'),

    #url(r'display_cross_sectional/$', views.cross_sectional2013, name='cross_sectional2013'),



    #County plots sections
    url(r'^$', views.county, name ='county'),
    url(r'(?P<R>[0-9]+)/(?P<C>[0-9]+)/(?P<Cat>[0-9]+)/$', views.county, name ='county'),

    url(r'display_plot/$', views.display_plot, name='display_plot'),

    #Forms
    url(r'^$', views.form, name ='form'),
##############################################################################

]
