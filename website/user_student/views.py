
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth import decorators, authenticate, login, logout
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from user_admin.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import *
from .Chep_Code_cua_anh_Quyet_AIdol import get

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


class edit_infor(LoginRequiredMixin, View):
    login_url = 'login:login'

    def get(self, request):
        role=request.user.role
        if role != 'S':
            return redirect('user_admin:logout')
        else:
            firstname = request.user.first_name
            lastname = request.user.last_name
            username=request.user.username
            email=request.user.email
            MSSV=request.user.IDnumber

        return render(request,'user_student/StudentChangeInformation.html',{'firstname':firstname}|{'lastname':lastname}|{'MSSV':MSSV}|{'username':username}|{'email':email})

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

            return redirect('user_student:main_screen')
       

class start_new_exam(LoginRequiredMixin, View):

    login_url = 'login:login'

    def get(self, request):
        role=request.user.role
        if role != 'S':
            return redirect('user_admin:logout')
        else:
            firstname = request.user.first_name
            lastname = request.user.last_name
            MSSV=request.user.IDnumber
            fm=StartNewExamForm()

            return render(request,'user_student/start_new_exam.html',{'firstname':firstname}|{'lastname':lastname}|{'fm':fm}|{'MSSV':MSSV})

    def post(self, request):
        fm=StartNewExamForm(request.POST)
        if fm.is_valid():
            ID_Subject = fm.cleaned_data['ID_Subject']
            NumQuestion = fm.cleaned_data['number_question']

            username = request.user.username
            un = MyUser.objects.get(pk=username)

            ex=Exam(ID_Subject=ID_Subject, User_Student=un, number_question=NumQuestion, flag='check')
            ex.save()

            a = Exam.objects.get(flag='check')
            i = a.id
            d = a.Date

            ex = Exam(id=i, Date=d, ID_Subject=ID_Subject, User_Student=un, number_question=NumQuestion, flag='none')
            ex.save()

            s=Subject.objects.get(Subject_Name=ID_Subject)
            ns=s.Subject_Name

            IDnumber = request.user.IDnumber
            firstname = request.user.first_name
            lastname = request.user.last_name

            ide = Exam.objects.get(pk=i)

            g = Grade(ID_Exam=ide, Grade=0, number_question=NumQuestion, number_correct_question=0, username = username,last_name =lastname,first_name = firstname, MSSV = IDnumber,exam_subject=ns, Date=d)
            g.save()

            return render(request, 'user_student/start_exam.html',{'MSSV':IDnumber}|{'Subj':ns} | {'IDexam':ide}|{'DateExam':d}|{'firstname':firstname}|{'lastname':lastname})



@decorators.login_required(login_url='/login/')
def new_exam(request, id):
    #if request.method == 'POST':
    #IDexam = request.POST.get('IDexam')
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    MSSV=request.user.IDnumber
    if role != 'S':
        return redirect('user_admin:logout')
    else:
        ide = Exam.objects.get(pk=id)
        ids=ide.ID_Subject_id
        NumQuestion=ide.number_question


    #***************************************


        id_list = QuestionBank.objects.filter(ID_Subject_id=ids)
        data = [e.get('id') for e in id_list.values("id")]
        print(data)
        IDquestion=get(data,NumQuestion)

    #****************************************
    

    for i in range(0,NumQuestion):
        idq=QuestionBank.objects.get(pk=IDquestion[i])
        dq=idq.Question_Detail

        sa=Students_Answer(ID_Exam=ide,ID_Question=idq,Students_Answer='0',Question_Detail=dq, Answer_Detail='0', flag=id*1000000+IDquestion[i])
        sa.save()

    list_question=Students_Answer.objects.filter(ID_Exam = id).values()
    return render(request,'user_student/question_list.html',{"listquest":list_question}|{'IDexam':ide}|{'lastname':lastname}|{'firstname':firstname}|{'MSSV':MSSV})



@decorators.login_required(login_url='login:login')
def detailView(request, ID_Question_id, ID_Exam_id):
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    MSSV=request.user.IDnumber
    if role != 'S':
        return redirect('user_admin:logout')
    else:
        qs = QuestionBank.objects.get(pk=ID_Question_id)
        a=QuestionAnswer.objects.filter(ID_Question=ID_Question_id).values()

        ide = Exam.objects.get(pk=ID_Exam_id)
        return render(request, "user_student/detail_question.html", {"qs": qs}|{"a":a}|{'IDexam':ide}|{'lastname':lastname}|{'firstname':firstname}|{'MSSV':MSSV})

@decorators.login_required(login_url='login:login')
def grade(request, ID_Question_id, id):
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    MSSV=request.user.IDnumber
    if role != 'S':
        return redirect('user_admin:logout')
    else:
        idq=QuestionBank.objects.get(pk=ID_Question_id)
        dq = idq.Question_Detail

        ide = Exam.objects.get(pk=id)

        a = Students_Answer.objects.get(flag=id * 1000000 + ID_Question_id)
        ID = a.id

        data = Grade.objects.get(ID_Exam=ide)
        i = data.id
        nq = data.number_question

        un = data.username
        firstname = data.first_name
        lastname = data.last_name
        IDnumber = data.MSSV
        ids = data.exam_subject
        d = data.Date

        dulieu = request.POST["choice"]
        ida = QuestionAnswer.objects.get(pk=dulieu)
        ad = ida.Question_Answer

        sa=Students_Answer(id=ID, ID_Exam=ide, ID_Question=idq, Question_Detail=dq, Students_Answer=dulieu, Answer_Detail=ad,flag=id*1000000+ID_Question_id)
        sa.save()

        data=CorrectAnswer.objects.get(ID_Question=idq)
        ca=data.Correct_Answer

        if ca==ad:
            data=Grade.objects.get(ID_Exam=ide)
            ncq=data.number_correct_question+1

            g = Grade(id=i, ID_Exam=ide, Grade=0, number_question=nq, number_correct_question=ncq, username=un, last_name=lastname, first_name=firstname, MSSV=IDnumber, exam_subject=ids, Date=d)
            g.save()


        list_question = Students_Answer.objects.filter(ID_Exam=ide).values()
        return render(request, 'user_student/question_list.html', {"listquest": list_question} | {'IDexam': ide}|{'lastname':lastname}|{'firstname':firstname}|{'MSSV':MSSV})


@decorators.login_required(login_url='login:login')
def end_exam(request, id):
    role=request.user.role
    if role != 'S':
        return redirect('user_admin:logout')
    else:
        ide = Exam.objects.get(pk=id)

        data = Grade.objects.get(ID_Exam=id)
        i = data.id
        nq = data.number_question
        ncq = data.number_correct_question
        point = ( 10 * ncq )/ nq

        un = data.username
        firstname = data.first_name
        lastname = data.last_name
        IDnumber = data.MSSV
        ids = data.exam_subject
        d = data.Date

        g = Grade(id=i, ID_Exam=ide, Grade=point, number_question=nq, number_correct_question=ncq, username =un ,last_name = lastname,first_name = firstname , MSSV = IDnumber ,exam_subject=ids, Date=d)
        g.save()

        return render(request, 'user_student/end_exam.html',{'point':point}|{'MSSV':IDnumber}|{'Subj':ids} | {'IDexam':ide}|{'DateExam':d}|{'firstname':firstname}|{'lastname':lastname})


@decorators.login_required(login_url='/login/')
def history_exam(request):
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    username=request.user.username
    MSSV=request.user.IDnumber
    if role != 'S':
        return redirect('user_admin:logout')
    else:
        if request.method =="POST":
            Search = request.POST['Search']
            SD=Grade.objects.filter(exam_subject__icontains= Search)
        else:
            #SD=MyUser.objects.filter(role='S')
            SD=Grade.objects.filter(username=username)
        paginator = Paginator(SD, 5) 
        page_number = request.GET.get('page')
        SD = paginator.get_page(page_number)
        return render(request, 'user_student/history_exam.html', {'SD' : SD}|{'lastname':lastname}|{'firstname':firstname}|{'MSSV':MSSV}|{'username':username})


class print_exam(LoginRequiredMixin, View):
    login_url = 'login:login'
    
    def get(self, request):
        role=request.user.role
    
        if role != 'S':
            return redirect('user_admin:logout')
        else:
            firstname = request.user.first_name
            lastname = request.user.last_name
            MSSV=request.user.IDnumber

            return render(request,'user_student/start_print_exam.html',{'firstname':firstname}|{'lastname':lastname}|{'MSSV':MSSV})

    def post(self, request):

        username = request.user.username

        IDexam= request.POST['IDexam']
        exam=Exam.objects.get(pk=IDexam)
        userexam=exam.User_Student_id
        if userexam != username:
            return HttpResponse("Đây là bài kiểm tra của tài khoản khác, bạn ko được quyền truy cập mã đề thi này !")
        else:
            NumQuestion=exam.number_question
            IDquestion_list = Students_Answer.objects.filter(ID_Exam_id=IDexam)
            IDquestion = [e.get('ID_Question_id') for e in IDquestion_list.values("ID_Question_id")]
           
            q2d=[]
            for a in range (0,NumQuestion):
                answer_list = QuestionAnswer.objects.filter(ID_Question_id=IDquestion[a])
                q1d = [e.get('Question_Answer') for e in answer_list.values("Question_Answer")]
                q2d.append(q1d)

            data=Students_Answer.objects.filter(ID_Exam_id=IDexam)

            g = Grade.objects.get(ID_Exam=IDexam)
            point = g.Grade
            firstname = g.first_name
            lastname = g.last_name
            IDnumber = g.MSSV
            ids = g.exam_subject
            d = g.Date

            return render(request,'user_student/print_exam.html',{'data':data}|{'q2d':q2d}|{'point':point}|{'MSSV':IDnumber}|{'Subj':ids} | {'IDexam':IDexam}|{'DateExam':d}|{'firstname':firstname}|{'lastname':lastname})