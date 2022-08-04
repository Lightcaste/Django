from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
id=''
s=''
em=''
pwd=''

#registration for teacher
def teacher(request):
    global fn,ln,id,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="MSGV":
                id=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        #c="insert into teacherinfor Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,id,s,em,pwd) 
        c="insert into teacherinfor (first_name,last_name,MSGV,sex,email,password) Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,id,s,em,pwd) 
        cursor.execute(c)
        m.commit()

    return render(request,'registrations/teacher.html')    



    # registration for student
def student(request):
    global fn,ln,id,s,em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="MSSV":
                id=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into studentinfor Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,id,s,em,pwd) 
        cursor.execute(c)
        m.commit()

    return render(request,'registrations/student.html')    