from django.urls import path
from .import views
from .views import edit_infor

app_name="user_teacher"
urlpatterns = [
    path('', views.Teacher_main,name='main_screen'),
    path('change-information', edit_infor.as_view(),name='teacher_change_information'),
    path('table-student',views.showStudent,name='show_student'),
    path('create-question',views.Create_Question,name='create-question'),

]

