from django.conf.urls import url
from album import views, models
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(views.base), name='base'),
    url(r'^category/$', views.category, name='category-list'),
    url(r'^category/(\d+)/detail/$', views.category_detail, name='category-detail'),
    url(r'^photo/$', views.PhotoListView.as_view(), name='photo-list'),
    url(r'^photo/(?P<pk>\d+)/detail/$', views.PhotoDetailView.as_view(), name='photo-detail'),
    url(r'^photo/(?P<pk>\d+)/update/$', views.PhotoUpdate.as_view(),name='photo-update'),
    #Create
    url(r'^photo/create/$', views.PhotoCreate.as_view(), name='photo-create'),
    #Delete
    url(r'^photo/(?P<pk>\d+)/delete/$', views.PhotoDelete.as_view(), name='photo-delete'),
    #Crear categoria
    url(r'^category/create/$', views.CategoryCreate.as_view(), name='category-create'),
    url(r'^certificado_egresado_pdf/$',views.CertificadoEgresadoPDF.as_view(), name='certificado_egresado_pdf'),  
    url(r'^buscar/$',views.Buscar, name='buscar-egresado'),  
    url(r'^egresado/create/$', views.EgresadoCreate.as_view(), name='egresado-create'),
    url(r'^listaEgresado/$', views.egresado_list, name='egresado-list'),
    url(r'^egresado/(\d+)/detail/$', views.egresado_detail, name='egresado-detail'),
    url(r'^egresado/(?P<pk>\d+)/delete/$', views.EgresadoDelete.as_view(), name='egresado-delete'),
    url(r'^egresado/(?P<pk>\d+)/update/$', views.EgresadoUpdate.as_view(), name='egresado-update'),
]