from django.conf.urls import patterns, include, url
from django.contrib import admin
import core.views as coreviews
from django.conf import settings
from django.conf.urls.static import static
from core.views import *
from core import views

admin.autodiscover()
#from django.conf.urls.media import media

urlpatterns = patterns('',
	url (r'^$', coreviews.LocationListView.as_view()),
	url (r'location/$', coreviews.LocationListView.as_view()),
	url(r'location/create/$', coreviews.LocationCreateView.as_view()),
	url(r'search/$', coreviews.SearchListView.as_view()),
	url(r'location/(?P<pk>\d+)/update/$', coreviews.LocationUpdateView.as_view(), name='location_update'),
	url(r'location/(?P<pk>\d+)/review/create/$', coreviews.ReviewCreateView.as_view(), name='review_create'),
	url(r'location/(?P<pk>\d+)/review/update/$', coreviews.ReviewUpdateView.as_view(), name='review_update'),
	url(r'entrance/$', coreviews.entrance),
	url(r'register/$', coreviews.register),
	(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
) 

urlpatterns += patterns('django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}), )