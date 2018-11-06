from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.principal),
    url(r'^detalle/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
    url(r'^post/nuevo/$', views.nuevo, name='nuevo'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar, name='editar'),
    url(r'^borrador/$', views.borrador, name='borrador'),
    url(r'^post/(?P<pk>\d+)/publish/$', views.paciente, name='paciente'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.eliminar, name='eliminar'),

    url(r'^lista/$', views.lista, name='lista'),
    url(r'^menu/$', views.menu, name='menu'),

    url(r'^base/$', views.base, name='base'),
]
