from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
id=''
s=''
em=''
pwd=''


# Create your views here.
def forgotpassTeaAction(request):
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
        c="insert into studentinfor Values('{}','{}','{}','{}','{}','{}')".format(fn,ln,id,s,em,pwd) #tuyệt đối phải có users "Values", k thì k nh
        cursor.execute(c)
        m.commit()

    return render(request,'forgotpassTea.php')    