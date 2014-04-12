from django.conf.urls import patterns, include, url
import simpler.views

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('', 
    # Examples:
    # url(r'^$', 'simpler.views.home', name='home'),
    # url(r'^simpler/', include('simpler.urls')),
    url(r'^$', simpler.views.home),
    url(r'^auth/login/$', simpler.views.login),

    url(r'^ermanager/', include('ermanager.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
