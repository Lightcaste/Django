from django.urls import path
from .import views

app_name="user_student"
urlpatterns = [
    path('', views.Student_main,name='main_screen'),
    path('change-information', views.Student_changing_information,name='student_change_information'),
    path('table-student',views.showStudent,name='show_student'),
    

]

