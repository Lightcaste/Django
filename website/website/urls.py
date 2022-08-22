"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from cgitb import html
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    # main screen
    path('', include ('main_screen.urls')),
    #login
    path('login/', include ('login.urls')),
    #registrations
    path('registrations/', include('registrations.urls')),   
    #user_admin
    path('userAdmin/', include ('user_admin.urls')),
    #user_teacher
    path('userTeacher/', include ('user_teacher.urls')),
    #user_student
    path('userStudent/', include ('user_student.urls')),
]
    