from django.http import HttpResponse
from msilib.schema import tables
from user_admin.models import MyUser
from django.views import View
from django.shortcuts import redirect, render
#import mysql.connector as sql
from django.contrib.auth import authenticate, login

class LoginClass(View):
    def get(self, request):
        return render (request,'login/loginAll.html')

    def post(self, request):
        USERNAME=request.POST.get('username')
        PASSWORD=request.POST.get('password')
        ROLE=request.POST.get('role')      
        my_user=authenticate(username=USERNAME, password=PASSWORD)
        if my_user is None:
            return HttpResponse("Dang nhap that con me no bai")
        
        user=MyUser.objects.get(pk=USERNAME)
        role=user.role
        if ROLE==role:
            if ROLE=='A':
                login(request, my_user)
                #return render (request,'user_admin/all.html')
                return redirect('user_admin:admin_main') 
            if ROLE=='S':
                login(request, my_user)
                return HttpResponse("day la trang sinh vien")    
            if ROLE=='T':
                login(request, my_user)
                return redirect('user_teacher:main_screen')   
        else:
            return HttpResponse("sai vai tro")