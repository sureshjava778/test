from django.contrib import admin
from django.urls import path
from vsapp import views

urlpatterns = [
    path('vsapp/test', views.test_view,name="test_view")
]