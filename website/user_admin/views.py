from django.shortcuts import render

def DataTeacher(request):

    return render(request,'user_admin/DataTeacher.html')

def DataStudent(request):

    return render(request,'user_admin/DataStudent.html')