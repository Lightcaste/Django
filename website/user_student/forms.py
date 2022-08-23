from django.forms import ModelForm
from user_admin.models import *

class StartNewExamForm(ModelForm):
    class Meta:
        model=Exam
        fields=['ID_Subject','number_question']