
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import decorators, authenticate, login, logout
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from user_admin.models import MyUser

@decorators.login_required(login_url='/login/')
def Student_main(request):
    role=request.user.role
    if role != 'S':
        return redirect('user_admin:logout')
    else:
        lastname=request.user.last_name
        firstname=request.user.first_name
        username=request.user.username
        email=request.user.email
        MSSV=request.user.IDnumber
        return render(request,'user_student/StudentMainPage.html',{'lastname':lastname}|{'firstname':firstname}|{'MSSV':MSSV}|{'username':username}|{'email':email})


@decorators.login_required(login_url='/login/')
def Student_changing_information(request):
    role=request.user.role
    if role != 'S':
        return redirect('user_admin:logout')
    else:
        lastname=request.user.last_name
        firstname=request.user.first_name
        username=request.user.username
        email=request.user.email
        MSSV=request.user.IDnumber
        return render(request,'user_student/StudentChangeInformation.html',{'lastname':lastname}|{'firstname':firstname}|{'MSSV':MSSV}|{'username':username}|{'email':email})



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
        paginator = Paginator(SD, 6) 
        page_number = request.GET.get('page')
        SD = paginator.get_page(page_number)
        return render(request, 'user_teacher/table_student.html', {'SD' : SD}|{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV}|{'username':username}|{'email':email})

    return render(request, 'user_teacher/table_student.html', {'SD' : SD}|{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV}|{'username':username}|{'email':email})


#@decorators.login_required(login_url='/login/')
#def Create_Question(request):
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