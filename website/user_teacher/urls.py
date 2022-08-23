from django.urls import path
from .import views
from .views import *

app_name="user_teacher"
urlpatterns = [
    path('', views.Teacher_main,name='main_screen'),
    path('change-information/', edit_infor.as_view(),name='teacher_change_information'),
    #path('choose_subject/',choose_subject.as_view(),name='choose_subject'),
    path('table-student/',views.showStudent,name='show_student'),
    path('create-question/',views.Create_Question,name='create-question'),
    path('question_bank/',views.question_bank,name='question_bank'),
    path('detailview/<int:ID_Question_id>', views.detailView, name='detailview'),
    path('add_new_question/',add_new_question.as_view(),name='add_new_question'),
   # path('grade_student/',views.grade_student,name="grade_student"),

]

