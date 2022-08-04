from django.urls import path
from .import views

urlpatterns = [
    path('teacher/', views.teacher),
    path('student/', views.student),
]

