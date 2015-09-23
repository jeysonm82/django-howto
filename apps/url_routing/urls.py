from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^2003/$', views.routing, name='single'), # Fixed value
    url(r'^([0-9]{4})/$', views.routing, name='4 digits'), # 4 digits number (from 0 to 9)
    url(r'^([0-9]{4})/([0-9]{2})/$', views.routing, name='4 and 2 digits'), # 4 digits and 2 digits numbers
    url(r'^([0-9]+)/$', views.routing, name='Arbitrary digits'), # Arbitrary digits number
]
