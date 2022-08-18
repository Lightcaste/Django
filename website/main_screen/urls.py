from django.urls import path
from .import views
app_name='main_screen'
urlpatterns = [
    path('', views.main_screen,name='main_screen'),
]

