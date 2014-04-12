from django.conf.urls import patterns, include, url
from ermanager import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpler.views.home', name='home'),
    # url(r'^simpler/', include('simpler.urls')),

    url(r'^bigscreen/$', views.big_board, name='big_screen'),

    url(r'^doctor_page/$',views.doctor_page, name='doctor_page'),

    url(r'^paitent/(?P<paitent_id>\d+)/$',views.paitent_edit,name='paitent'),
    )
