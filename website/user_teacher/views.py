
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.views import View

from user_admin.models import MyUser

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import decorators, authenticate, login, logout

@decorators.login_required(login_url='/login/')
def Teacher_main(request):
    role=request.user.role
    if role != 'T':
        return redirect('user_admin:logout')
    else:
        lastname=request.user.last_name
        firstname=request.user.first_name
        username=request.user.username
        email=request.user.email
        MSGV=request.user.IDnumber
        return render(request,'user_teacher/TeacherMainPage.html',{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV}|{'username':username}|{'email':email})






class edit_infor(LoginRequiredMixin, View):
    login_url = 'login:login'

    def get(self, request):
        role=request.user.role
        if role != 'T':
            return redirect('user_admin:logout')
        else:
            firstname = request.user.first_name
            lastname = request.user.last_name
            username=request.user.username
            email=request.user.email
            MSGV=request.user.IDnumber

        return render(request,'user_teacher/TeacherChangeInformation.html',{'firstname':firstname}|{'lastname':lastname}|{'MSGV':MSGV}|{'username':username}|{'email':email})

    def post(self, request):
      
            username = request.user.username
            password = request.user.password
            role = request.user.role
            is_staff = request.user.is_staff

            new_first_name = request.POST.get('first_name')
            new_last_name = request.POST.get('last_name')
            new_IDnumber = request.POST.get('IDnumber')
            new_email = request.POST.get('email')

            edit_infor = MyUser(username=username,password=password,role=role,is_staff=is_staff, first_name=new_first_name, last_name=new_last_name, IDnumber=new_IDnumber,
                                email=new_email)
            edit_infor.save()

            return redirect('user_teacher:main_screen')
       
           








@decorators.login_required(login_url='/login/')
def showStudent(request):
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    username=request.user.username
    email=request.user.email
    MSGV=request.user.IDnumber
    if role != 'T':
        return redirect('user_admin:logout')
    else:
        if request.method =="POST":
            Search = request.POST['Search']
            SD=MyUser.objects.filter(last_name__icontains= Search)
        else:
            SD=MyUser.objects.filter(role='S')
        paginator = Paginator(SD, 5) 
        page_number = request.GET.get('page')
        SD = paginator.get_page(page_number)
        return render(request, 'user_teacher/table_student.html', {'SD' : SD}|{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV}|{'username':username}|{'email':email})

    return render(request, 'user_teacher/table_student.html', {'SD' : SD}|{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV}|{'username':username}|{'email':email})


@decorators.login_required(login_url='/login/')
def Create_Question(request):
    role=request.user.role
    if role != 'T':
        return redirect('user_admin:logout')
    else:
        lastname=request.user.last_name
        firstname=request.user.first_name
        username=request.user.username
        email=request.user.email
        MSGV=request.user.IDnumber
        return render(request,'user_teacher/create_questions.html',{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV}|{'username':username}|{'email':email})