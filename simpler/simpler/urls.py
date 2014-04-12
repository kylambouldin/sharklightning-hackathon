from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^ERManager/',include('ermanager.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
