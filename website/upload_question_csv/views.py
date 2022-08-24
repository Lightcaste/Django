from django.shortcuts import render, redirect
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

from .models import QuestionBankCSV
from user_admin.models import QuestionBank, QuestionAnswer, CorrectAnswer

# Create your views here.
class upload_question_csv(LoginRequiredMixin, View):
    login_url = 'login:login'

    def get(self, request):
        firstname = request.user.first_name
        lastname = request.user.last_name

        return render(request, 'upload_question_csv/upload_question_csv.html',{'firstname': firstname} | {'lastname': lastname})

    def post(self, request):
        NQ = request.POST.get('NumQuestion')
        NumQuestion=int(NQ)
        for i in range(1,NumQuestion+1):
            data=QuestionBankCSV.objects.get(stt=i)
            id=data.id

            qsd=data.Question_Detail
            qi=data.Question_Image
            ids=data.ID_Subject

            qa=data.Question_AnswerA
            qb=data.Question_AnswerB
            qc=data.Question_AnswerC
            qd=data.Question_AnswerD

            ca=data.Correct_Answer

            QB=QuestionBank(Question_Detail=qsd,Question_Image=qi,ID_Subject_id=ids)
            QB.save()

            QB=QuestionBank.objects.get(Question_Detail=qsd)
            idq=QB.id

            QA=QuestionAnswer(ID_Question_id=idq,Question_Answer=qa)
            QA.save()
            QA = QuestionAnswer(ID_Question_id=idq, Question_Answer=qb)
            QA.save()
            QA = QuestionAnswer(ID_Question_id=idq, Question_Answer=qc)
            QA.save()
            QA = QuestionAnswer(ID_Question_id=idq, Question_Answer=qd)
            QA.save()

            CA= CorrectAnswer(ID_Question_id=idq, Correct_Answer=ca)
            CA.save()

            QBCSV=QuestionBankCSV(id=id,Question_Detail=qsd,Question_Image=qi,ID_Subject=ids,Question_AnswerA=qa,Question_AnswerB=qb,Question_AnswerC=qc,Question_AnswerD=qd,Correct_Answer=ca,stt=0)
            QBCSV.save()

        return redirect('user_teacher:question_bank')