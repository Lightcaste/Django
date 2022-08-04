from django.urls import path
from .import views

urlpatterns = [
    path('teacher/', views.DataTeacher),
    path('student/', views.DataStudent),
]

