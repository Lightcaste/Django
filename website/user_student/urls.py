from django.urls import path
from .import views
from .views import edit_infor
app_name="user_student"
urlpatterns = [
    path('', views.Student_main,name='main_screen'),
    path('change-information', edit_infor.as_view(),name='student_change_information'),
    path('table-student',views.showStudent,name='show_student'),
    path('new-exam',views.new_exam,name='new-exam'),
    

]

