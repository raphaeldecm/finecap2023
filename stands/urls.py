from django.urls import path

from . import views

app_name = "stands"
urlpatterns = [
    path('', views.index, name='index'),
]
