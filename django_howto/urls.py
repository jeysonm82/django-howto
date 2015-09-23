from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'browser.views.home', name='home'),
     url(r'^view/(?P<app_name>.+)$', 'browser.views.view_example', name='view'),
     url(r'^routing/', include('apps.url_routing.urls')),
     url(r'^admin/', include(admin.site.urls)),
)
