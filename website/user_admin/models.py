from enum import unique
from django.db import connections
from django.db import models
from django.forms import ModelForm, Textarea
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class MyUser(AbstractUser):
    role_choice= (
        ('A', "Admin",),
        ('S', "Student",),
        ('T', "Teacher",),
        )
    role = models.CharField(max_length=1,choices=role_choice,)
    #username = None
    username=models.CharField(max_length=50, primary_key= True)
    IDnumber=models.CharField(max_length=50, unique = True) 
    #is_staff = models.BooleanField(default=True)
    #is_active = models.BooleanField(default=True)
    #is_superuser = models.BooleanField(default=True)
    # is_admin =  models.BooleanField(default=True)
    last_login = None
    date_joined = None
    #email = models.EmailField(_('email address'), unique=True)
    #USERNAME_FIELD = 'email'
   # REQUIRED_FIELDS = []
    


    
    #date_joined = None
    #is_superuser = None
    #is_staff = None
    #is_active = None




            # Môn học
class Subject(models.Model):
        Subject_Name=models.TextField(max_length=255)
        class Meta:
            db_table='subject'
# Ngân hàng câu hỏi
class QuestionBank(models.Model):
        Question_Detail=models.TextField(max_length=99999)
        Question_Image=models.TextField(max_length=99999999, default=None)
        ID_Subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
        class Meta:
            db_table='question_bank'
# Bảng đáp án câu hỏi
class QuestionAnswer(models.Model):
        ID_Question=models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
        Question_Answer=models.TextField(max_length=99999)
        class Meta:
            db_table='question_answer'
# Bảng đáp án đúng
class CorrectAnswer(models.Model):
        ID_Question=models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
        Correct_Answer=models.TextField(max_length=99999)
        class Meta:
            db_table='correct_answer'

# Đề thi
class Exam(models.Model):
        Date=models.DateTimeField(auto_now=True)
        ID_Subject=models.ForeignKey(Subject, on_delete=models.CASCADE)
        MSSV=models.ForeignKey(MyUser, on_delete=models.CASCADE)
        class Meta:
            db_table='exam'
# Đáp án thí sinh
class Students_Answer(models.Model):
        ID=models.IntegerField(primary_key=True)
        ID_Question=models.ForeignKey(QuestionBank, on_delete=models.CASCADE)
        ID_Exam=models.ForeignKey(Exam, on_delete=models.CASCADE)
        Students_Answer=models.IntegerField()
        class Meta:
            db_table='student_answer'
            unique_together=(("ID_Question","ID_Exam"),)
# điểm
class Grade(models.Model):
        ID_Exam=models.ForeignKey(Exam, on_delete=models.CASCADE, null=True)
        Grade=models.CharField(max_length=10)
        class Meta:
            db_table='grade'



