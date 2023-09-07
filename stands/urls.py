from django.urls import path

from . import views

app_name = "stands"
urlpatterns = [
    path('', views.index, name='index'),
    path('reservas/list/', views.reservas_list, name='reservas-list'),
    path('reservas/detail/<int:id>/', views.reservas_detail, name='reservas-detail'),
    path('reservas/update/<int:id>/', views.reservas_update, name='reservas-update'),
    path('reservas/delete/<int:id>/', views.reservas_delete, name='reservas-delete'),
    path('reservas/create/', views.reservas_create, name='reservas-create'),
]
