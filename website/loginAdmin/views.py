from msilib.schema import tables
from django.shortcuts import redirect, render
import mysql.connector as sql

id=''
pwd=''


# Create your views here.
def loginAdminAction(request):
    global em,pwd
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="MSQT":
                id=value
            if key=="password":
                pwd=value
        c="select * from adinfor where MSQT= '{}' and password ='{}'".format(id,pwd) #insert là nhập, select là chọn
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,'loginAdmin.html')
        else:
           # return render(request.get('https://www.youtube.com/watch?v=tytTIoigrd8'))
            return redirect('https://www.youtube.com/watch?v=tytTIoigrd8')
    return render(request,'loginAdmin.html')    