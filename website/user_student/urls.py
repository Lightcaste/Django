from django.urls import path
from .import views
from .views import edit_infor,start_new_exam


app_name='user_student'
urlpatterns=[
    path('', views.Student_main,name='main_screen'),
    path('change-information', edit_infor.as_view(),name='student_change_information'),
    path('start_new_exam/',start_new_exam.as_view(),name='start_new_exam'),
    path('new_exam/<int:id>/',views.new_exam,name='new_exam'),
    path('detailview/<int:ID_Exam_id>/<int:ID_Question_id>/', views.detailView, name='detailview'),
    path('grade/<int:id>/<int:ID_Question_id>/',views.grade,name='grade'),
    path('end_exam/<int:id>',views.end_exam,name='end_exam'),
    path('history_exam/',views.history_exam,name='history_exam'),

]