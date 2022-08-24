from django.urls import path
from .import views
from .views import upload_question_csv


app_name='upload_question_csv'
urlpatterns=[
    path('',upload_question_csv.as_view(),name='upload_question_csv'),

]