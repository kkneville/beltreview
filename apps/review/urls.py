from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.dashboard, name="dashboard"),
    url(r'^dashboard$', views.dashboard, name="dashboard"),

    url(r'^(?P<id>\d+)/showmember$', views.showmember, name="showmember"),

    url(r'^(?P<id>\d+)/showbook$', views.showbook, name="showbook"),

    url(r'^addreview$', views.addreview, name="addreview"),

    url(r'^bookreview$', views.bookreview, name="bookreview"),

    url(r'^add$', views.add, name="add"),

    url(r'^(?P<id>\d+)/deletereview$', views.deletereview, name="deletereview"),

    url(r'^logout$', views.logout, name="logout"),
]
