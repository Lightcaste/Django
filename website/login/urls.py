from django.urls import path
from .import views

urlpatterns = [
    path('admin/', views.loginAdmin),
    path('student/', views.loginStudent),
    path('teacher/', views.loginTeacher),
]

