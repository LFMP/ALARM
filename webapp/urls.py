from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^adapterlist', views.adapterlist, name='adapterlist'),
    url(r'^add', views.add, name='add')]
