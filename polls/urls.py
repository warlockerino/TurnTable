from django.conf.urls import include, url
from . import views
app_name = 'polls'

urlpatterns = [
   
    url(r'^$', views.IndexView.as_view() , name='index'),
    # ex: /polls/5/
    url(r'^(?P<pk>\d+)/$',views.DetailView.as_view(), name='detail'), 
    #url('^(?P<question_id>\d+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>\d+)/vote/$', views.vote, name='vote'),

]