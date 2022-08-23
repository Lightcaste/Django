from django.forms import ModelForm
from user_admin.models import *
from django import forms


class EditInforForm(ModelForm):
    class Meta:
        model=MyUser
        fields=['first_name','last_name','IDnumber','email']

class AddNewQuestionForm(ModelForm):
    class Meta:
        model=QuestionBank
        fields=['Question_Detail','Question_Image','ID_Subject']
       
            
class AddNewAnswerForm(ModelForm):
    class Meta:
        model=QuestionAnswer
        fields=['Question_Answer']

class AddNewCorrectAnswerForm(ModelForm):
    class Meta:
        model=CorrectAnswer
        fields=['Correct_Answer']
        