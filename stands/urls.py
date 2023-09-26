from django.urls import path

from . import views

app_name = "stands"
urlpatterns = [
    path('stands/list/', views.StandsListView.as_view(), name='stands-list'),
    path('stands/detail/<int:pk>/', views.StandDetailView.as_view(), name='stands-detail'),
    path('stands/update/<int:pk>/', views.StandUpdateView.as_view(), name='stands-update'),
    path('stands/delete/<int:pk>/', views.StandDeleteView.as_view(), name='stands-delete'),
    path('stands/create/', views.StandCreateView.as_view(), name='stands-create'),
]
