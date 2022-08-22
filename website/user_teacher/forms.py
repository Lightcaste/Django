from django.forms import ModelForm
from user_admin.models import MyUser
from user_admin.models import QuestionBank, QuestionAnswer, CorrectAnswer

class EditInforForm(ModelForm):
    class Meta:
        model=MyUser
        fields=['first_name','last_name','IDnumber','email']