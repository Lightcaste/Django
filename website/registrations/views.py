from django.shortcuts import render
import mysql.connector as sql
from user_admin.models import MyUser
fn=''
ln=''
id=''
rl=''
em=''
pwd=''
ur=''
su='0'
sf='1'
ac='1'
#registration for teacher
def registrations(request):
    global fn,ln,id,rl,em,pwd,su,sf,ac,ur
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='website')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="IDnumber":
                id=value
            if key=="role":
                rl=value
            if key=="username":
                ur=value
            if key=="email":
                em=value
            if key=="password":
                pwd=value
        c="insert into user_admin_myuser (first_name,last_name,IDnumber,role,email,password,username,is_superuser,is_staff,is_active) Values('{}','{}','{}','{}','{}','{}','{}','0','1','1')".format(fn,ln,id,rl,em,pwd,ur,su,sf,ac) 
        cursor.execute(c)
        m.commit()

        user=MyUser.objects.get(pk=ur)
        user.set_password(pwd)
        user.save()
    
    return render(request,'registrations/registrations.html')    