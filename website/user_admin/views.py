from django.http import HttpRequest
from django.shortcuts import redirect, render, HttpResponse
from django.core.paginator import Paginator
from user_admin.models import MyUser
from user_admin.forms import TeacherDetailForm
from django.http.response import HttpResponse
from django.contrib.auth import decorators, authenticate, login, logout


@decorators.login_required(login_url='/login/')
def Admin_main(request):
    role=request.user.role
    if role != 'A':
        return redirect('user_admin:logout')
    else:
        lastname=request.user.last_name
        firstname=request.user.first_name

    return render(request,'user_admin/all.html',{'lastname':lastname}|{'firstname':firstname})

# hàm tìm kiếm, xóa, lấy thông tin giảng viên
@decorators.login_required(login_url='/login/')
def showTeacher(request):
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    if role != 'A':
        return redirect('user_admin:logout')
    else:
        if request.method =="POST":
            Search = request.POST['Search']
            TD=MyUser.objects.filter(last_name__icontains= Search) 
        else:
            TD=MyUser.objects.filter(role='T')
            paginator = Paginator(TD, 5) 
            page_number = request.GET.get('page')
            TD = paginator.get_page(page_number)
            #return render(request, 'user_admin/table_teacher.html', {'TD' : TD})
    return render(request, 'user_admin/table_teacher.html', {'TD' : TD}|{'lastname':lastname}|{'firstname':firstname})

            

@decorators.login_required(login_url='/login/')
def delete(request, username):
    TD=MyUser.objects.get(pk=username)
    TD.delete()
    return redirect('/userAdmin/tableTeacher')

# như trên nhưng sinh viên
@decorators.login_required(login_url='/login/')
def showStudent(request):
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    if role != 'A':
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
    return render(request, 'user_admin/table_student.html', {'SD' : SD}|{'lastname':lastname}|{'firstname':firstname})

@decorators.login_required(login_url='/login/')
def deleteSD(request, username):
    SD=MyUser.objects.get(pk=username)
    SD.delete()
    return redirect('/userAdmin/tableStudent')

def logout_view(request):
    logout(request)
    return redirect('main_screen:main_screen')