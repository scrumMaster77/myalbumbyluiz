from django.conf.urls import url
from album import views

urlpatterns = [
    url(r'^$', views.base, name='base'),
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
     #Delete categoria
    url(r'^category/(?P<category_id>\d+)/delete/$', views.CategoryDelete.as_view(), name='category-delete'),
    ]
