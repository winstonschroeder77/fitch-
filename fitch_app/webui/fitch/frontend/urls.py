from django.conf.urls import url

from . import views

app_name = 'frontend'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
#    url(r'^$', views.home, name='home'),
]

