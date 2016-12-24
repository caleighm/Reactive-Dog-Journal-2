from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.entry_list, name='entry_list'),
	url(r'^entry/(?P<pk>\d+)/$', views.entry_detail, name='entry_detail'),
]