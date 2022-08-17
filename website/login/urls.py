from django.urls import path
from django.contrib import admin
from .views import LoginClass

app_name='login'
urlpatterns = [
    path('',LoginClass.as_view(), name='login'),
]

