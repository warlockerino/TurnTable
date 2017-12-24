from django.conf.urls import include, url
from django.contrib import admin
from profiles import urls
from tables import urls
urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^tables/', include('tables.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^admin/', admin.site.urls),
]
