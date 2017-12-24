from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^create/$', views.createTable.as_view() , name='create_table'),
    url(r'^(?P<table_name>\w+)/$', views.table, name='table'),
    #url(r'^(?P<table_name>\w+)/join/$', views.table_join, name='table_join'),
    #url(r'^(?P<table_name>\w+)/admin/$', views.table_admin, name='table_admin'),
    url(r'^$', views.tables , name='table_list'),

]
