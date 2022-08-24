
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.core.paginator import Paginator
from django.views import View

from user_admin.models import *

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import decorators, authenticate, login, logout

from .forms import *
from user_student.forms import *

@decorators.login_required(login_url='/login/')
def Teacher_main(request):
    role=request.user.role
    if role != 'T':
        return redirect('user_admin:logout')
    else:
        lastname=request.user.last_name
        firstname=request.user.first_name
        username=request.user.username
        email=request.user.email
        MSGV=request.user.IDnumber
        return render(request,'user_teacher/TeacherMainPage.html',{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV}|{'username':username}|{'email':email})

class edit_infor(LoginRequiredMixin, View):
    login_url = 'login:login'

    def get(self, request):
        role=request.user.role
        if role != 'T':
            return redirect('user_admin:logout')
        else:
            firstname = request.user.first_name
            lastname = request.user.last_name
            username=request.user.username
            email=request.user.email
            MSGV=request.user.IDnumber

        return render(request,'user_teacher/TeacherChangeInformation.html',{'firstname':firstname}|{'lastname':lastname}|{'MSGV':MSGV}|{'username':username}|{'email':email})

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

            return redirect('user_teacher:main_screen')
       

@decorators.login_required(login_url='/login/')
def Create_Question(request):

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


@decorators.login_required(login_url='login:login')
def question_bank(request):
    role=request.user.role
    if role != 'T':
        return redirect('user_admin:logout')
    else:
        firstname = request.user.first_name
        lastname = request.user.last_name
        MSGV=request.user.IDnumber

        list_question = QuestionBank.objects.all()

        return render(request,'user_teacher/question_list.html',{'firstname':firstname}|{'lastname':lastname}|{"listquest":list_question}|{'MSGV':MSGV})


@decorators.login_required(login_url='login:login')
def detailView(request, ID_Question_id):
    role=request.user.role
    if role != 'T':
        return redirect('user_admin:logout')
    else:
        firstname = request.user.first_name
        lastname = request.user.last_name

        qs = QuestionBank.objects.get(pk=ID_Question_id)
        a=QuestionAnswer.objects.filter(ID_Question=ID_Question_id).values()
        ca=CorrectAnswer.objects.filter(ID_Question=ID_Question_id).values()

        return render(request, "user_teacher/detail_question.html", {"qs": qs}|{"a":a}|{'ca':ca}|{'firstname':firstname}|{'lastname':lastname})


class add_new_question(LoginRequiredMixin, View):
    login_url = 'login:login'

    def get(self, request):
        firstname = request.user.first_name
        lastname = request.user.last_name
        MSGV=request.user.IDnumber

        role=request.user.role
        if role != 'T':
            return redirect('user_admin:logout')
        else:
            nq=AddNewQuestionForm()
            nca=AddNewCorrectAnswerForm()

            return render(request,'user_teacher/add_new_question.html',{'firstname':firstname}|{'lastname':lastname}|{'nq':nq}|{'nca':nca}|{'MSGV':MSGV})

    def post(self, request):
        nq=AddNewQuestionForm(request.POST)
        nca=AddNewCorrectAnswerForm(request.POST)

        dapan1 = request.POST.get('dapan1')
        dapan2 = request.POST.get('dapan2')
        dapan3 = request.POST.get('dapan3')
        dapan4 = request.POST.get('dapan4')

        if nq.is_valid() and nca.is_valid():
            qd = nq.cleaned_data['Question_Detail']
            qi = nq.cleaned_data['Question_Image']
            ids = nq.cleaned_data['ID_Subject']
            ca = nca.cleaned_data['Correct_Answer']

            NewQuestion = QuestionBank(Question_Detail=qd,Question_Image=qi,ID_Subject=ids)
            NewQuestion.save()

            a = QuestionBank.objects.get(Question_Detail=qd)
            b = a.id
            ID = QuestionBank.objects.get(pk=b)

            NewCorrect = CorrectAnswer(Correct_Answer=ca, ID_Question= ID)
            NewCorrect.save()

            NewAnswer = QuestionAnswer(Question_Answer=dapan1, ID_Question= ID)
            NewAnswer.save()
            NewAnswer = QuestionAnswer(Question_Answer=dapan2, ID_Question=ID)
            NewAnswer.save()
            NewAnswer = QuestionAnswer(Question_Answer=dapan3, ID_Question=ID)
            NewAnswer.save()
            NewAnswer = QuestionAnswer(Question_Answer=dapan4, ID_Question=ID)
            NewAnswer.save()


            return redirect('user_teacher:add_new_question')
        else:
            return HttpResponse('Ban nhap sai du lieu roi')



@decorators.login_required(login_url='/login/')
def showStudent(request):
    role=request.user.role
    lastname=request.user.last_name
    firstname=request.user.first_name
    MSGV=request.user.IDnumber
    if role != 'T':
        return redirect('user_admin:logout')
    else:
        

        if request.method =="POST":
            Search = request.POST['Search']
            SD=Grade.objects.filter(last_name__icontains=Search) | Grade.objects.filter(exam_subject__icontains=Search)
        else:
            SD=Grade.objects.all()
        paginator = Paginator(SD, 5) 
        page_number = request.GET.get('page')
        SD = paginator.get_page(page_number)
        return render(request, 'user_teacher/table_student.html', {'SD' : SD}|{'lastname':lastname}|{'firstname':firstname}|{'MSGV':MSGV})


#class choose_subject(LoginRequiredMixin, View):
    login_url = 'login:login'

    def get(self,request):
        return render (request,'choose_subject.html') 
    def post(self, request):
        subject=StartNewExamForm(request.POST)
        showStudent(request, subject)
      