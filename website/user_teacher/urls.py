from django.urls import path
from .import views

app_name="user_teacher"
urlpatterns = [
    path('', views.Teacher_main,name='main_screen'),
    path('change-information', views.Teacher_changing_information,name='teacher_change_information'),
    path('table-student',views.showStudent,name='show_student'),
    path('create-question',views.showStudent,name='create-question'),

]

