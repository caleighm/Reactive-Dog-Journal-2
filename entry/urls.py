from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.entry_list, name='entry_list'),
	url(r'^entry/(?P<pk>\d+)/$', views.entry_detail, name='entry_detail'),
	url(r'^entry/new/$', views.entry_new, name='entry_new'),
	url(r'^entry/(?P<pk>\d+)/edit/$', views.entry_edit, name='entry_edit'),
	url(r'^entry/(?P<pk>\d+)/remove/$', views.entry_remove, name='entry_remove'),
	url(r'^entry/report/$', views.entry_report, name='entry_report'),
]