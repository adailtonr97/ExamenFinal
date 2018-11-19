from django.conf.urls import include, url
from . import views


urlpatterns = [
    url(r'^$', views.principal),

    url(r'^detalle/(?P<pk>[0-9]+)/$', views.detalle, name='detalle'),
    url(r'^detalle2/(?P<pk>[0-9]+)/$', views.detalle2, name='detalle2'),

    url(r'^post/nuevo/$', views.nuevo, name='nuevo'),
    url(r'^post/nuevo2/$', views.nuevo2, name='nuevo2'),

    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.editar, name='editar'),
    url(r'^post/(?P<pk>[0-9]+)/edit2/$', views.editar2, name='editar2'),

    url(r'^post/(?P<pk>\d+)/publish/$', views.grado, name='grado'),
    url(r'^post/(?P<pk>\d+)/publish2/$', views.materia, name='materia'),

    url(r'^post/(?P<pk>\d+)/remove/$', views.eliminar, name='eliminar'),
    url(r'^post/(?P<pk>\d+)/remove2/$', views.eliminar2, name='eliminar2'),

    url(r'^lista/$', views.lista, name='lista'),
    url(r'^lista2/$', views.lista2, name='lista2'),

    url(r'^base/$', views.base, name='base'),
    url(r'^base2/$', views.base2, name='base2'),
]
