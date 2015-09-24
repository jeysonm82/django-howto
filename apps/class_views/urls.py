from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^/basic/$', views.BasicView.as_view(), name='class_based_views'),
    url(r'^/template/$', views.TemplateViewSample.as_view(), name='class_based_views_template'), 
]
