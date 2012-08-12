from django.conf.urls import patterns, include, url
from django.views.generic import ListView
from route.models import Trip


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	#url(r'^$', 'route.views.index'),
    url(r'^$',
        ListView.as_view(
        queryset=Trip.objects.all(),
        context_object_name='latest_trips',
        template_name='index.html')),
    url(r'^trips/add/$','route.views.trip_add'), 
	url(r'^trips/(?P<trip_id>\d+)/$', 'route.views.trip_edit'),
    

    #url(r'^trips/add/$', 'route.views.add_trip'), 


    # Examples:
    # url(r'^$', 'truckapp.views.home', name='home'),
    # url(r'^truckapp/', include('truckapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
