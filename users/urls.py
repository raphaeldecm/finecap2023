from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "users"
urlpatterns = [
    path('users/form/', views.UserCreateView.as_view(), name='create'),
    path('users/list/', views.UsersListView.as_view(), name='list'),
    # Users authentication
    path('authentication/login/', auth_views.LoginView.as_view(), name='login'),
    path('authentication/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
