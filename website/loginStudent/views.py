from msilib.schema import tables
from django.shortcuts import redirect, render
import mysql.connector as sql

em=''
pwd=''


# Create your views here.
def loginStudentAction(request):
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
        c="select * from studentinfor where email= '{}' and password ='{}'".format(em,pwd) #insert là nhập, select là chọn
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'loginStudent.html')
        else:
           # return render(request.get('https://www.youtube.com/watch?v=tytTIoigrd8'))
            return redirect('https://www.youtube.com/watch?v=tytTIoigrd8')
    return render(request,'loginStudent.html')    