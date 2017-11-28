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
    url(r'^buscar/$',views.buscar, name='buscar-egresado'),  
    #Crear egresado
    url(r'^egresado/create/$', views.EgresadoCreate.as_view(), name='egresado-create'),
    url(r'^listaEgresado/$', views.egresado_list, name='egresado-list'),
    url(r'^egresado/(\d+)/detail/$', views.egresado_detail, name='egresado-detail'),
    url(r'^egresado/(?P<pk>\d+)/delete/$', views.EgresadoDelete.as_view(), name='egresado-delete'),
    url(r'^egresado/(?P<pk>\d+)/update/$', views.EgresadoUpdate.as_view(), name='egresado-update'),
    #crear facultad
    url(r'^facultad/create/$', views.FacultadCreate.as_view(), name='facultad-create'),
    url(r'^listaFacultades/$', views.facultad_list, name='facultad-list'),
    url(r'^facultad/(\d+)/detail/$', views.facultad_detail, name='facultad-detail'),
    url(r'^facultad/(?P<pk>\d+)/delete/$', views.FacultadDelete.as_view(), name='facultad-delete'),
    url(r'^facultad/(?P<pk>\d+)/update/$', views.FacultadUpdate.as_view(), name='facultad-update'),
    #crear programa
    url(r'^programa/create/$', views.ProgramaCreate.as_view(), name='programa-create'),
    url(r'^listaProgramas/$', views.programa_list, name='programa-list'),
    url(r'^programa/(\d+)/detail/$', views.programa_detail, name='programa-detail'),
    url(r'^programa/(?P<pk>\d+)/delete/$', views.ProgramaDelete.as_view(), name='programa-delete'),
    url(r'^programa/(?P<pk>\d+)/update/$', views.ProgramaUpdate.as_view(), name='programa-update'),
    #crear modalidad
    url(r'^modalidad/create/$', views.ModalidadCreate.as_view(), name='modalidad-create'),
    url(r'^listaModalidad/$', views.modalidad_list, name='modalidad-list'),
    url(r'^modalidad/(\d+)/detail/$', views.modalidad_detail, name='modalidad-detail'),
    url(r'^modalidad/(?P<pk>\d+)/delete/$', views.ModalidadDelete.as_view(), name='modalidad-delete'),
    url(r'^modalidad/(?P<pk>\d+)/update/$', views.ModalidadUpdate.as_view(), name='modalidad-update'),
     #crear tipo pago
    url(r'^tipo_pago/create/$', views.Tipo_pagoCreate.as_view(), name='tipo_pago-create'),
    url(r'^listaTipoPago/$', views.tipo_pago_list, name='tipo_pago-list'),
    url(r'^tipo_pago/(\d+)/detail/$', views.tipo_pago_detail, name='tipo_pago-detail'),
    url(r'^tipo_pago/(?P<pk>\d+)/delete/$', views.Tipo_pagoDelete.as_view(), name='tipo_pago-delete'),
    url(r'^tipo_pago/(?P<pk>\d+)/update/$', views.Tipo_pagoUpdate.as_view(), name='tipo_pago-update'),
]