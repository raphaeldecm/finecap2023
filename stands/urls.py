from django.urls import path

from . import views

app_name = "stands"
urlpatterns = [
    path('', views.HomeView.as_view(), name='index'),
    path('reservas/list/', views.ReservasListView.as_view(), name='reservas-list'),
    path('reservas/detail/<int:pk>/', views.ReservaDetailView.as_view(), name='reservas-detail'),
    path('reservas/update/<int:pk>/', views.ReservaUpdateView.as_view(), name='reservas-update'),
    path('reservas/delete/<int:pk>/', views.ReservaDeleteView.as_view(), name='reservas-delete'),
    path('reservas/create/', views.ReservaCreateView.as_view(), name='reservas-create'),
]
