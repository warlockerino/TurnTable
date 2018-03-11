from django.conf.urls import include, url
from django.contrib import admin
from Turntable.views import login_redirect
from profiles import urls
from profiles import views
from django.contrib.auth.views import login
from polls import urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', login_redirect, name='login-redirect'),
    url(r'^register/$', views.register,name='register'),
    url(r'^profile/edit/', views.edit_profile, name='edit_profile'),
    url(r'^login/$', login, {'template_name':'login.html'}),
    url(r'^logout/$', login, {'template_name':'logout.html'}),
    url(r'^profile/',include('profiles.urls')),
    url(r'^tables/',include('tables.urls')),
    url(r'^polls/',include('polls.urls')),


]