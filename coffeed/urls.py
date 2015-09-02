from django.conf.urls import include, url, patterns
from django.contrib import admin
import core.views as coreviews
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coffeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'', include('core.urls')),
    url(r'location/(?P<pk>\d+)/detail/$', coreviews.LocationDetailView.as_view(), name='location_list'),
)

#urlpatterns += patterns('django.views.static',(r'^media/(?P<path>.*)','serve',{'document_root':settings.MEDIA_ROOT}), )