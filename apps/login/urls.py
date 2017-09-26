from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^index$', views.index, name="index"),
    url(r'^login$', views.login, name="login"),
    url(r'^addmember$', views.addmember, name="addmember"),
    url(r'^logout$', views.logout, name="logout"),
]
