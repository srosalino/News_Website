from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registo/', views.registoUser, name='registo'),
    path('noticias/', views.noticias, name='noticias'),
    path('site_noticia/<int:noticia_id>/', views.detalhe, name='detalhe'),
]
