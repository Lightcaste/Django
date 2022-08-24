from django.contrib import admin
from .models import QuestionBankCSV

from django.shortcuts import render

from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect

from django.urls import path
from django.urls import reverse


# Register your models here.
class CsvImportFrom(forms.Form):
    csv_upload=forms.FileField()

class QuestionBankCSVAdmin(admin.ModelAdmin):
    list_display = ('Question_Detail','Question_AnswerA','Question_AnswerB','Question_AnswerC','Question_AnswerD')

    def get_urls(self):
        urls = super().get_urls()
        new_urls=[path('upload-csv/',self.upload_csv),]
        return new_urls + urls

    def upload_csv(self, request):

        if request.method == "POST":
            csv_file = request.FILES["csv_upload"]

            if not csv_file.name.endswith('.csv'):
                messages.warning(request, 'The wrong file type was uploaded')
                return HttpResponseRedirect(request.path_info)

            file_data = csv_file.read().decode("utf-8")
            csv_data = file_data.split("\n")

            for x in csv_data:
                fields = x.split(",")
                created = QuestionBankCSV.objects.update_or_create(
                    Question_Detail=fields[0],
                    Question_Image=fields[1],
                    ID_Subject=fields[2],
                    Question_AnswerA=fields[3],
                    Question_AnswerB=fields[4],
                    Question_AnswerC=fields[5],
                    Question_AnswerD=fields[6],
                    Correct_Answer=fields[7],
                    stt=fields[8],
                )
            url = reverse('upload_question_csv:upload_question_csv')
            return HttpResponseRedirect(url)


        form=CsvImportFrom()
        data={"form":form}
        return render(request,"admin/csv_upload.html",data)

admin.site.register(QuestionBankCSV, QuestionBankCSVAdmin)