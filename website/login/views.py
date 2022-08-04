# login for admin

from django.http import HttpResponse
from msilib.schema import tables
from django.shortcuts import redirect, render
import mysql.connector as sql

id=''
pwd=''
em=''
def loginAdmin(request):
    global id,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="MSQT":
                id=value
            if key=="password":
                pwd=value
        c="select * from adinfor where MSQT= '{}' and password ='{}'".format(id,pwd) 
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'login/loginAdmin.html')
        else:
           # return render(request.get('https://www.youtube.com/watch?v=tytTIoigrd8'))
            return redirect('https://www.youtube.com/watch?v=tytTIoigrd8')
    return render(request,'login/loginAdmin.html')    


    # Login for student

def loginStudent(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from studentinfor where email= '{}' and password ='{}'".format(em,pwd) 
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'login/loginStudent.html')
        else:
           # return render(request.get('https://www.youtube.com/watch?v=tytTIoigrd8'))
            return redirect('https://www.youtube.com/watch?v=tytTIoigrd8')
    return render(request,'login/loginStudent.html')  



    #login for teacher
    
def loginTeacher(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="select * from teacherinfor where email= '{}' and password ='{}'".format(em,pwd) 
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'login/loginTeacher.html')
        else:
           # return render(request.get('https://www.youtube.com/watch?v=tytTIoigrd8'))
            return redirect('https://www.youtube.com/watch?v=tytTIoigrd8')
    return render(request,'login/loginTeacher.html')    