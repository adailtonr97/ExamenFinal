from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^pub/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
    url(r'^post/new/$', views.nuevo, name='nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar, name='editar'),
]
