from django.urls import path
from .import views

app_name="userAdmin"
urlpatterns = [
    path('', views.Admin_main,name="Admin_main"),
    path('tableTeacher/', views.showTeacher),
    path('tableTeacher/delete/<int:id>', views.delete),
    path('tableStudent/', views.showStudent),
    path('tableStudent/delete/<int:id>', views.delete),
    path('logout/',views.logout_view,name="logout"),
]

