from django import forms
from user_admin.models import MyUser
from django.forms import fields
class TeacherDetailForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = "__all__"

class StudentForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = "__all__"
    
class MyForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['role',]