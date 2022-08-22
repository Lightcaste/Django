from django.urls import path
from .import views

app_name="user_admin"
urlpatterns = [
    path('', views.Admin_main,name="admin_main"),
    path('tableTeacher/', views.showTeacher,name="table_teacher"),
    path('tableTeacher/delete/<username>', views.delete),
    path('tableStudent/', views.showStudent,name="table_student"),
    path('tableStudent/delete/<username>', views.delete),
    path('logout/',views.logout_view,name="logout"),
]

