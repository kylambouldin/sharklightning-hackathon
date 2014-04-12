#URLS For ERManager
from django.conf.urls import patterns, url

from ermanager import views

urlpatterns = patterns('',
  url(r'^doctor_page/$',views.doctor_page, name='doctor_page'),

  url(r'^paitent/(?P<paitent_id>\d+)/$',views.paitent_edit,name='paitent'),
)
