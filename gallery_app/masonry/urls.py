from django.conf.urls import patterns, url

from masonry import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^water_color$', views.water_color, name='water_color'), 
                       url(r'^digital$', views.digital, name='digital'), 
                       url(r'^contact/', views.contact, name='contact')
                      )

