from django.conf.urls import url
from django.contrib import admin
from main.views import Home, upload

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^upload/$', upload, name='upload'),
    url(r'^$', Home.as_view(), name='home'),
]