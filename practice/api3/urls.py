from django.urls import path
from . import views

urlpatterns = [
    path('', views.addData),
    path('get', views.getData)
]